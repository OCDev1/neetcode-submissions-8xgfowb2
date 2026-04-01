class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        self.res = False

        def helper(i ,j ,cur_word):
            if cur_word == word:    # we found our word
                self.res = True
                return
            if i < 0 or i >= rows:  # out of bounds
                return
            if j < 0 or j >= cols:  # out of bounds
                return

            # append letter to cur word if not visited yet and cur word can still be word
            if board[i][j] != "$" and len(cur_word) < len(word):
                cur_word = cur_word + board[i][j]
                og_letter = board[i][j]     # save so we can restore later
                board[i][j] = "$"   # mark as visited
            else:
                return
            
            # explore all valid paths
            helper(i, j-1, cur_word)    # up
            helper(i, j+1, cur_word)    # down
            helper(i-1, j, cur_word)    # left
            helper(i+1, j, cur_word)    # right
            
            # restore original letter for next iterations
            board[i][j] = og_letter

        # run the search starting from every cell
        for i in range(rows):
            for j in range(cols):
                # search only if letter matches first letter of word
                if board[i][j] == word[0]:
                    helper(i,j,"")
        
        return self.res