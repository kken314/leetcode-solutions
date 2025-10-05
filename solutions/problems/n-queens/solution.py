class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isSafe(board, row, col):
            for r in range(row):
                if board[r][col] == 'Q':
                    return False
            r, c = row-1, col-1
            while r >= 0 and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1
            r, c = row - 1, col + 1
            while r >= 0 and c < n:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c += 1

            return True

        def Nqueens(board, row):
            if row == n:
                result.append(["".join(r) for r in board])
                return
            for col in range(n):
                if isSafe(board, row, col):
                    board[row][col] = 'Q'
                    Nqueens(board, row+1)
                    board[row][col] = '.'

        result = []
        empty_board = [["." for _ in range(n)] for _ in range(n)]
        Nqueens(empty_board, 0)
        return result