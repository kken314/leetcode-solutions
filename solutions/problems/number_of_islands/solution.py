class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        def bfs(row, col):
            q = deque()
            q.append((row, col))
            while q:
                r, c = q.pop()
                grid[r][c] = '0'
                if r - 1 in range(rows) and c in range(cols) and grid[r - 1][c] == '1':
                    q.append((r - 1, c))
                if r + 1 in range(rows) and c in range(cols) and grid[r + 1][c] == '1':
                    q.append((r + 1, c))
                if r in range(rows) and c - 1 in range(cols) and grid[r][c - 1] == '1':
                    q.append((r, c - 1))
                if r in range(rows) and c + 1 in range(cols) and grid[r][c + 1] == '1':
                    q.append((r, c + 1))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    bfs(row, col)
                    islands += 1
        return islands