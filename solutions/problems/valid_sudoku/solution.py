class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            s = set()
            for col in range(9):
                if board[row][col] in s:
                    return False
                elif board[row][col] != '.':
                    s.add(board[row][col])
        
        for col in range(9):
            s = set()
            for row in range(9):
                if board[row][col] in s:
                    return False
                elif board[row][col] != '.':
                    s.add(board[row][col]) 

        point = [(0, 0), (0, 3), (0, 6),
                 (3, 0), (3, 3), (3, 6),
                 (6, 0), (6, 3), (6, 6)]

        for i, j in point:
            s = set()
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    if board[row][col] in s:
                        return False
                    elif board[row][col] != '.':
                        s.add(board[row][col]) 
        return True