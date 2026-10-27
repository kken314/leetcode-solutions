import json
import os
import re
import subprocess
import urllib.parse
from pathlib import Path

import requests

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
SOLUTIONS_PATH = Path("solutions/problems")
if not SOLUTIONS_PATH.is_dir():
    SOLUTIONS_PATH = Path("solutions")

README_PATH = Path("README.md")
EASY_PATH = Path("EASY.md")
MEDIUM_PATH = Path("MEDIUM.md")
HARD_PATH = Path("HARD.md")

LEETCODE_API = "https://leetcode.com/api/problems/algorithms/"
TAGS_DATASET_URL = (
    "https://raw.githubusercontent.com/WilliamZhang20/"
    "leetcode-clusters/master/data/problems.json"
)
REQUEST_TIMEOUT = 20

DIFFICULTY = {1: "Easy", 2: "Medium", 3: "Hard"}
DIFFICULTY_EMOJI = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}
DIFFICULTY_BADGE = {
    "Easy": "🟢 Easy",
    "Medium": "🟡 Medium",
    "Hard": "🔴 Hard",
    "Unknown": "⚪ Unknown",
    "-": "➖",
}


def normalize_key(value: str) -> str:
    """Normalize names/slugs to make folder matching more forgiving."""
    return re.sub(r"[^a-z0-9]", "", value.lower())


def get_json(url: str, *, timeout: int = REQUEST_TIMEOUT):
    response = requests.get(
        url,
        timeout=timeout,
        headers={"User-Agent": "Mozilla/5.0 LeetCode-README-Generator"},
    )
    response.raise_for_status()
    return response.json()


def load_problem_map():
    """Fetch LeetCode's problem catalogue and index it by slug/title."""
    print("🌐 Fetching LeetCode problem catalogue...")
    payload = get_json(LEETCODE_API)
    problem_map = {}

    for item in payload.get("stat_status_pairs", []):
        stat = item.get("stat", {})
        title = stat.get("question__title", "").strip()
        slug = stat.get("question__title_slug", "")
        question_id = stat.get("frontend_question_id")

        if not title or not slug or question_id is None:
            continue

        problem = {
            "id": int(question_id),
            "title": title,
            "difficulty": DIFFICULTY.get(
                item.get("difficulty", {}).get("level"), "Unknown"
            ),
            "slug": slug,
        }
        problem_map[slug] = problem
        problem_map[normalize_key(slug)] = problem
        problem_map[normalize_key(title)] = problem

    return problem_map


def load_tags_map():
    """Load topic tags from the community dataset; gracefully fall back if absent."""
    print("🏷️  Fetching topic tags...")
    tags_map = {}

    try:
        payload = get_json(TAGS_DATASET_URL, timeout=15)
        tag_names = {
            tag.get("slug"): tag.get("name")
            for tag in payload.get("tags", [])
            if tag.get("slug") and tag.get("name")
        }

        for problem in payload.get("problems", []):
            slug = problem.get("slug", "")
            title = problem.get("title", "")
            tags = [
                tag_names.get(tag, tag.replace("-", " ").title())
                for tag in problem.get("tags", [])
            ]

            if slug:
                tags_map[slug] = tags
                tags_map[normalize_key(slug)] = tags
            if title:
                tags_map[normalize_key(title)] = tags

    except (requests.RequestException, ValueError, KeyError, TypeError) as error:
        print(f"⚠️  Topic dataset unavailable: {error}")

    return tags_map


def fetch_tags_fallback(slug: str):
    """Query LeetCode GraphQL for tags if the community dataset has no entry."""
    query = """
    query questionTopics($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        topicTags { name }
      }
    }
    """
    try:
        response = requests.post(
            "https://leetcode.com/graphql",
            json={"query": query, "variables": {"titleSlug": slug}},
            headers={
                "Content-Type": "application/json",
                "Referer": "https://leetcode.com",
                "User-Agent": "Mozilla/5.0",
            },
            timeout=10,
        )
        response.raise_for_status()
        payload = response.json()
        question = payload.get("data", {}).get("question") or {}
        return [tag["name"] for tag in question.get("topicTags", [])]
    except (requests.RequestException, ValueError, KeyError, TypeError):
        return []


def find_problem(folder: str, problem_map: dict):
    """Match a solution folder to LeetCode's slug/title catalogue."""
    slug = folder.replace("_", "-").lower()
    return problem_map.get(slug) or problem_map.get(normalize_key(folder))


def markdown_escape(value: str) -> str:
    """Keep titles/tags from breaking Markdown tables."""
    return str(value).replace("|", r"\|").replace("\n", " ")


def code_link(folder: str) -> str:
    encoded = urllib.parse.quote(folder)
    return f"[View Code ↗](./{SOLUTIONS_PATH.as_posix()}/{encoded})"


def generate_markdown_table(problem_list, include_difficulty=True):
    if include_difficulty:
        header = (
            "| # | Problem | Difficulty | Topics | Solution |\n"
            "|:--:|:---|:--:|:---|:--:|\n"
        )
    else:
        header = (
            "| # | Problem | Topics | Solution |\n"
            "|:--:|:---|:---|:--:|\n"
        )

    rows = []
    for problem in problem_list:
        question_id = problem["id"] if problem["id"] != 9999 else "—"
        title = markdown_escape(problem["title"])
        topics = ", ".join(
            f"`{markdown_escape(tag)}`" for tag in problem["tags"]
        ) or "—"
        link = problem["link"]

        if include_difficulty:
            difficulty = DIFFICULTY_BADGE.get(
                problem["difficulty"], problem["difficulty"]
            )
            rows.append(
                f"| {question_id} | {title} | {difficulty} | {topics} | {link} |"
            )
        else:
            rows.append(f"| {question_id} | {title} | {topics} | {link} |")

    return header + "\n".join(rows) + "\n"


def build_problem_list(problem_map, tags_map):
    if not SOLUTIONS_PATH.is_dir():
        raise FileNotFoundError(
            f"Cannot find a solutions directory. Checked: "
            f"'solutions/problems' and 'solutions'."
        )

    folders = sorted(
        path.name for path in SOLUTIONS_PATH.iterdir() if path.is_dir()
    )
    print(f"📂 Found {len(folders)} solution folders.")

    problems = []
    for folder in folders:
        info = find_problem(folder, problem_map)
        slug = info["slug"] if info else folder.replace("_", "-").lower()
        key = normalize_key(folder)

        tags = tags_map.get(slug)
        if tags is None:
            tags = tags_map.get(key)
        if tags is None and info:
            tags = fetch_tags_fallback(info["slug"])
        tags = tags or []

        problems.append({
            "id": info["id"] if info else 9999,
            "title": info["title"] if info else folder.replace("_", " ").title(),
            "difficulty": info["difficulty"] if info else "Unknown",
            "tags": tags,
            "link": code_link(folder),
        })

    return sorted(problems, key=lambda problem: (problem["id"], problem["title"]))


def difficulty_card(emoji, label, count, filename):
    return (
        f'<a href="{filename}">'
        f'<img src="https://img.shields.io/badge/{label}-{count}-'
        f'{ {"Easy": "2ea44f", "Medium": "d4a72c", "Hard": "cf222e"}[label] }'
        f'?style=for-the-badge&logo=leetcode&logoColor=white" alt="{label} problems">'
        f"</a>"
    )


def build_readme(problems, easy, medium, hard):
    total = len(problems)
    matched = sum(problem["id"] != 9999 for problem in problems)
    unknown = total - matched

    # SVG-style badge images and HTML are supported by GitHub README rendering.
    content = [
        '<div align="center">',
        "",
        "# ⚡ LeetCode — Problem Archive",
        "",
        "*A growing collection of solutions, patterns, and algorithm practice.*",
        "",
        f'<img src="https://img.shields.io/badge/Problems-{total}-blue?style=for-the-badge&logo=leetcode&logoColor=white" alt="Total problems">',
        f'<img src="https://img.shields.io/badge/Easy-{len(easy)}-2ea44f?style=for-the-badge" alt="Easy">',
        f'<img src="https://img.shields.io/badge/Medium-{len(medium)}-d4a72c?style=for-the-badge" alt="Medium">',
        f'<img src="https://img.shields.io/badge/Hard-{len(hard)}-cf222e?style=for-the-badge" alt="Hard">',
        "",
        "[📚 Browse All](#-problem-index) · "
        "[🟢 Easy](./EASY.md) · "
        "[🟡 Medium](./MEDIUM.md) · "
        "[🔴 Hard](./HARD.md)",
        "",
        "</div>",
        "",
        "---",
        "",
        "## 📊 Repository Overview",
        "",
        "| Metric | Count |",
        "|:---|---:|",
        f"| 🧩 Total solution folders | **{total}** |",
        f"| 🟢 Easy | **{len(easy)}** |",
        f"| 🟡 Medium | **{len(medium)}** |",
        f"| 🔴 Hard | **{len(hard)}** |",
        f"| 🔎 Matched with LeetCode catalogue | **{matched}** |",
    ]

    if unknown:
        content.append(f"| ⚠️ Unmatched folders | **{unknown}** |")

    content.extend([
        "",
        "## 🧭 Problems by Difficulty",
        "",
        "| Easy | Medium | Hard |",
        "|:---:|:---:|:---:|",
        f"| [🟢 **{len(easy)} problems**](./EASY.md) "
        f"| [🟡 **{len(medium)} problems**](./MEDIUM.md) "
        f"| [🔴 **{len(hard)} problems**](./HARD.md) |",
        "",
        "## 🧠 Problem Index",
        "",
        f"> Browse **{total}** solution folders, sorted by LeetCode problem number.",
        "",
        generate_markdown_table(problems, include_difficulty=True),
        "",
        "---",
        "",
        "<details>",
        "<summary>⚙️ How this repository is generated</summary>",
        "",
        "This README is generated by a Python script that scans the solution folders, "
        "matches problems against LeetCode's catalogue, and adds topic tags where available.",
        "",
        "### Run locally",
        "",
        "```bash",
        "python generate_readme.py",
        "```",
        "",
        "Install the dependency first if needed:",
        "",
        "```bash",
        "python -m pip install requests",
        "```",
        "",
        "### Optional GitHub Actions sync",
        "",
        "You can automate syncing with a workflow. Store `LEETCODE_SESSION` and "
        "`CSRF_TOKEN` as repository Actions secrets; never commit session cookies "
        "or tokens to source control.",
        "",
        "</details>",
        "",
        "<div align=\"center\">",
        "",
        "*Built with consistency, one problem at a time. 🚀*",
        "",
        "</div>",
        "",
    ])
    return "\n".join(content)


def build_difficulty_page(title, emoji, problems, other_links):
    content = [
        f"# {emoji} LeetCode {title} Problems",
        "",
        f"> **{len(problems)} problems** · Keep learning, keep shipping.",
        "",
        " | ".join(other_links),
        "",
        "---",
        "",
        generate_markdown_table(problems, include_difficulty=False),
        "",
        "[⬆️ Back to top](./README.md)",
        "",
    ]
    return "\n".join(content)


def write_file(path: Path, content: str):
    path.write_text(content, encoding="utf-8")
    print(f"✅ Generated {path}")


def main():
    if not SOLUTIONS_PATH.is_dir():
        raise SystemExit(
            "❌ Could not find 'solutions/problems' or 'solutions'. "
            "Run this script from the repository root."
        )

    try:
        problem_map = load_problem_map()
    except (requests.RequestException, ValueError) as error:
        raise SystemExit(
            f"❌ Could not fetch the LeetCode catalogue: {error}\n"
            "Check your internet connection and try again."
        )

    tags_map = load_tags_map()
    problems = build_problem_list(problem_map, tags_map)

    easy = [p for p in problems if p["difficulty"] == "Easy"]
    medium = [p for p in problems if p["difficulty"] == "Medium"]
    hard = [p for p in problems if p["difficulty"] == "Hard"]

    write_file(README_PATH, build_readme(problems, easy, medium, hard))
    write_file(
        EASY_PATH,
        build_difficulty_page(
            "Easy", "🟢", easy,
            ["[⬅️ All Problems](./README.md)", "[🟡 Medium](./MEDIUM.md)", "[🔴 Hard](./HARD.md)"],
        ),
    )
    write_file(
        MEDIUM_PATH,
        build_difficulty_page(
            "Medium", "🟡", medium,
            ["[🟢 Easy](./EASY.md)", "[⬅️ All Problems](./README.md)", "[🔴 Hard](./HARD.md)"],
        ),
    )
    write_file(
        HARD_PATH,
        build_difficulty_page(
            "Hard", "🔴", hard,
            ["[🟢 Easy](./EASY.md)", "[🟡 Medium](./MEDIUM.md)", "[⬅️ All Problems](./README.md)"],
        ),
    )

    print(
        f"\n🎉 Done! {len(problems)} problems indexed "
        f"({len(easy)} Easy · {len(medium)} Medium · {len(hard)} Hard)."
    )


if __name__ == "__main__":
    main()
