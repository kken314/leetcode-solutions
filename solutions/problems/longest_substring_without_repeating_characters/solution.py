class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        substring = set()
        longest = 0

        for right in range(len(s)):
            while s[right] in substring:
                substring.remove(s[left])
                left += 1
            longest = max(longest, right - left + 1)
            substring.add(s[right])
        return longest
