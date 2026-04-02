class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkRows(board) and self.checkCols(board) and self.checkSubBoxes(board)
    
    def checkRows(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for cell in row:
                if cell == '.':
                    continue
                elif cell in seen:
                    return False
                else:
                    seen.add(cell)
        return True
    
    def checkCols(self, board: List[List[str]]) -> bool:
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] == '.':
                    continue
                elif board[row][col] in seen:
                    return False
                else:
                    seen.add(board[row][col])
        return True

    def checkSubBoxes(self, board: List[List[str]]) -> bool:
        for box_row in range(3):
            for box_col in range(3):
                seen = set()
                for r in range(3):
                    for c in range(3):
                        if board[box_row * 3 + r][box_col * 3 + c] == '.':
                            continue
                        elif board[box_row * 3 + r][box_col * 3 + c] in seen:
                            return False
                        else:
                            seen.add(board[box_row * 3 + r][box_col * 3 + c])
        return True