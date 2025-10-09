class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for r in range(1, rowIndex + 1):
            res.append(res[-1] * (rowIndex - r + 1) // r)
        return res
        