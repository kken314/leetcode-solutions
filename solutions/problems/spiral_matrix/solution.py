class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        up = 0
        down = len(matrix) - 1
        right = len(matrix[0]) - 1
        left = 0
        res = []
        while up <= down and left <= right:
            for col in range(left, right + 1):
                res.append(matrix[up][col])
            up += 1
            for row in range(up, down + 1):
                res.append(matrix[row][right])
            right -= 1
            if up <= down:
                for col in range(right, left - 1, -1):
                    res.append(matrix[down][col])
                down -= 1
            if right >= left:
                for row in range(down, up - 1, -1):
                    res.append(matrix[row][left])
                left += 1
        return res