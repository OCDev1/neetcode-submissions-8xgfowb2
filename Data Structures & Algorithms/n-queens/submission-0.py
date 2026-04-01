class Solution:
    def solveNQueens(self, n: int):
        res = []

        # create the board
        board = [["."] * n for i in range(n)]
        
        # helper function
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if self.isSafe(r, c, board):
                    board[r][c] = "Q"
                    backtrack(r + 1)
                    board[r][c] = "."

        backtrack(0)
        return res

    # function to check if current queen placement is legal
    # Note: we are placing queens from top to bottom row so we only need to check cells above current queen
    def isSafe(self, r: int, c: int, board):

        # check vertically upwards
        row = r - 1
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row -= 1
            
        # check diagonal to up and left
        row, col = r - 1, c - 1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        # check diagonal to up and left
        row, col = r - 1, c + 1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1
        return True