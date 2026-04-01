class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        self.res = False

        def helper(i ,j ,cur_word):
            if cur_word == word:
                self.res = True
                return
            if i < 0 or i >= rows:
                return
            if j < 0 or j >= cols:
                return

            # append letter to cur word if not visited yet and cur word can still be word
            if board[i][j] != "$" and len(cur_word) < len(word):
                cur_word = cur_word + board[i][j]
                og_letter = board[i][j]
                board[i][j] = "$"
            else:
                return
            
            # up
            helper(i, j-1, cur_word)
            # down
            helper(i, j+1, cur_word)
            # left
            helper(i-1, j, cur_word)
            # right
            helper(i+1, j, cur_word)
            
            # return original letter
            board[i][j] = og_letter

        # run the search starting from every cell
        for i in range(rows):
            for j in range(cols):
                helper(i,j,"")
        
        return self.res