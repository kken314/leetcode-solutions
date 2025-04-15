class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            sorted_word = tuple(sorted(word))
            result[sorted_word].append(word)
        return list(result.values())