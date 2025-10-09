class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            char_ascii = columnNumber % 26
            res.append(chr(ord('A') + char_ascii))
            columnNumber //= 26
        return ''.join(res[::-1])