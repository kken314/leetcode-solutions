class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        def around(row, col):
            count = 0
            if row - 1 >= 0 and grid[row - 1][col] == 1:
                count += 1
            if row + 1 < len(grid) and grid[row + 1][col] == 1:
                count += 1
            if col - 1 >= 0 and grid[row][col - 1] == 1:
                count += 1
            if col + 1 < len(grid[0]) and grid[row][col + 1] == 1:
                count += 1
            return count

        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    res += 4 - around(row, col)
        return res