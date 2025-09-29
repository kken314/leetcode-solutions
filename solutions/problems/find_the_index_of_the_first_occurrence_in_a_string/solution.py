class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        N = len(haystack)
        n = len(needle)
        for i in range(0, N - n + 1):
            if haystack[i:i+n] == needle:
                return i
        return -1