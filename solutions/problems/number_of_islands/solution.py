class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        count = 0
        def delete_land(grid, r, c):
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] != '1':
                return
            grid[r][c] = '0'
            delete_land(grid, r + 1, c)
            delete_land(grid, r - 1, c)
            delete_land(grid, r, c + 1)
            delete_land(grid, r, c - 1)
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    delete_land(grid, r, c)
                    count += 1
        return count
