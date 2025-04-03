class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l = []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        while top <= bottom and right >= left:
            for col in range (left, right + 1):
                l.append(matrix[top][col])
            top += 1
            for row in range(top, bottom + 1):
                l.append(matrix[row][right])
            right -= 1
            if top <= bottom:
                for col in range(right, left-1, -1):
                    l.append(matrix[bottom][col])
                bottom -= 1
            if right >= left:
                for row in range(bottom, top - 1, -1):
                    l.append(matrix[row][left])
                left += 1
        return l
