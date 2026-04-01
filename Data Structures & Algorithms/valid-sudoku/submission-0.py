class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #create hash sets
        cols=defaultdict(set)
        rows=defaultdict(set)
        squares=defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                #check if the value is in relevant sets
                if(
                    board[i][j] in cols[j]
                    or board[i][j] in rows[i]
                    or board[i][j] in squares[int(i/3),int(j/3)]
                ):
                    return False

                #add current value to hash sets
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[int(i/3),int(j/3)].add(board[i][j])
        
        return True
