class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        result = []
        while True:
            if p1 < len(word1):
                result.append(word1[p1])
                p1 += 1
            if p2 < len(word2):
                result.append(word2[p2])
                p2 += 1
            if p1 >= len(word1) and p2 >= len(word2):
                return ''.join(result)