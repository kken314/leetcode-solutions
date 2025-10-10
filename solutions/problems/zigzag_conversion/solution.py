class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        zz = [['-'] * len(s) for _ in range(numRows)]
        row = 0
        col = 0
        state = 'down'
        for c in s:
            zz[row][col] = c
            if state == 'down':
                if row == numRows - 1:
                    state = 'up'
                    row -= 1
                    col += 1
                else:
                    row += 1
            else:  # up
                if row == 0:
                    state = 'down'
                    row += 1
                else:
                    row -= 1
                    col += 1
        res = []
        for row in range(numRows):
            for col in range(len(s)):
                if zz[row][col] != '-':
                    res.append(zz[row][col])
        return ''.join(res)