class Solution:
    def scoreBalance(self, s: str) -> bool:
        print(ord('a'))
        sumleft = 0
        sumright = 0
        for c in s:
            sumright += ord(c) - 96
        for c in s:
            if sumleft == sumright:
                return True
            sumleft += ord(c) - 96
            sumright -= ord(c) - 96
        return False
            