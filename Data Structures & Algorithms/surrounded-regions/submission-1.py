class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(i,j):
            # if we are at an X, or already visited this cell, or out of bounds-return
            if i >= ROWS or i < 0 or j >= COLS or j < 0 or board[i][j] == "#" or board[i][j] == "X" or (i,j) in visited:
                return

            # we reached this O from the borders, so mark as safe
            if board[i][j] == "O":
                board[i][j] = "#"
            
            visited.add((i,j))  # add to visited to prevent double checking and infinite loops
            
            # recursive calls
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        # run DFS from border Os
        for i in range(ROWS):
            if board[i][0] == "O":
                dfs(i,0)
            if board[i][COLS-1] == "O":
                dfs(i,COLS-1)
        
        for j in range(COLS):
            if board[0][j] == "O":
                dfs(0,j)
            if board[ROWS-1][j] == "O":
                dfs(ROWS-1,j)

        # configure final table
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":  # Os that are surrounded
                    board[i][j] = "X"
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "#":  # safe Os
                    board[i][j] = "O"


