class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board),len(board[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        def inBounds(r: int,c: int) -> bool:
            if (0 <= r < rows) and (0<=c<cols):
                return True
            else:
                return False
        
        def replaceOs(r,c):
            if not inBounds(r,c):
                return
            if board[r][c] == 'O':
                board[r][c] = 'T'   # for temp
                for dr,dc in directions:
                    replaceOs(r+dr,c+dc)
            return
        
        for r in range(rows):
            replaceOs(r,0)
            replaceOs(r,cols-1)
        for c in range(cols):
            replaceOs(0,c)
            replaceOs(rows-1,c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'