class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(i,j):
            if i >= ROWS or i < 0 or j >= COLS or j < 0 or board[i][j] == "#" or board[i][j] == "X" or (i,j) in visited:
                return

            # mark as safe
            if board[i][j] == "O":
                board[i][j] = "#"
            
            visited.add((i,j))
            
            # recursive calls
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)


        # run on border Os
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
                if board[i][j] == "O":
                    board[i][j] = "X"
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "#":
                    board[i][j] = "O"


