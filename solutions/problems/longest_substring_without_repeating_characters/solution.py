class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        set1 = set()
        longest = 0

        for R in range (len(s)):
            while s[R] in set1:
                set1.remove(s[L])
                L+=1
            w = (R-L)+1
            longest = max(longest, w)
            set1.add(s[R])
        return longest
