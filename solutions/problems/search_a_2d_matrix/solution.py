class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols - 1
        while right >= left:
            mid = (left + right) // 2
            row = mid // cols
            col = mid % cols
            curr = matrix[row][col]
            if curr == target:
                return True
            elif curr < target:
                left = mid + 1
            else:
                right = mid - 1
        return False 