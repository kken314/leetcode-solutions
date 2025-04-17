class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            j = i
            k = 0
            while haystack[j] == needle[k] and j < len(haystack):
                if k == len(needle) - 1:
                    return i
                j += 1
                k += 1
        return -1