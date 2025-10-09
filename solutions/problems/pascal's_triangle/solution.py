class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        PascalTri = []
        for i in range(numRows):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    e = 1
                else:
                    prevRow = PascalTri[-1]
                    e = prevRow[j - 1] + prevRow[j]
                row.append(e)
            PascalTri.append(row)
        return PascalTri