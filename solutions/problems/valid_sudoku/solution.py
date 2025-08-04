class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range(9):
            nums = set()
            for col in range(9):
                p = board[row][col]
                if p in nums:
                    return False
                elif p != '.':
                    nums.add(p)

        for col in range(9):
            nums = set()
            for row in range(9):
                p = board[row][col]
                if p in nums:
                    return False
                elif p != '.':
                    nums.add(p)

        point = [(0, 0), (0, 3), (0, 6),
                 (3, 0), (3, 3), (3, 6),
                 (6, 0), (6, 3), (6, 6)]

        for x, y in point:
            nums = set()
            for row in range(x, x + 3):
                for col in range(y, y + 3):
                    p = board[row][col]
                    if p in nums:
                        return False
                    elif p != '.':
                        nums.add(p)

        return True