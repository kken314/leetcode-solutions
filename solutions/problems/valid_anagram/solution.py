class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charUse = {}
        for char in s:
            if char in charUse:
                charUse[char] += 1
            else:
                charUse[char] = 1
        for char in t:
            if char not in charUse or charUse[char] == 0:
                return False
            charUse[char] -= 1
        return True
            
