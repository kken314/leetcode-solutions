class Solution:
    def reverseVowels(self, s: str) -> str:
        p1 = 0
        p2 = len(s) - 1
        s = list(s)
        vowels = set('aeiouAEIOU')
        while p1 < p2:
            while p1 < p2 and s[p1] not in vowels:
                p1 += 1
            while p1 < p2 and s[p2] not in vowels:
                p2 -= 1
            s[p1], s[p2] = s[p2], s[p1]
            p1 += 1
            p2 -= 1
        return ''.join(s)
