class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0
        for letter in t:
            if s_index >= len(s):break
            if letter == s[s_index]:
                s_index += 1
        if s_index == len(s):
            return True
        return False
