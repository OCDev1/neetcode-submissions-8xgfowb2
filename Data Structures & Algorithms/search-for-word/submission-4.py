class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def helper(i ,j ,cur_word):
            if cur_word == word:    # we found our word
                return True
            if i < 0 or i >= rows:  # out of bounds
                return False
            if j < 0 or j >= cols:  # out of bounds
                return False

            # append letter to cur word if not visited yet and cur word can still be word
            if board[i][j] != "$" and len(cur_word) < len(word):
                cur_word = cur_word + board[i][j]
                og_letter = board[i][j]     # save so we can restore later
                board[i][j] = "$"   # mark as visited
            else:
                return False
            
            # explore all valid paths and check if one contains our word
            res = (
            helper(i, j-1, cur_word)    # up
            or helper(i, j+1, cur_word)    # down
            or helper(i-1, j, cur_word)    # left
            or helper(i+1, j, cur_word)    # right
            )

            # restore original letter for next iterations
            board[i][j] = og_letter
            return res

        # run the search starting from every cell
        for i in range(rows):
            for j in range(cols):
                # search only if letter matches first letter of word
                if board[i][j] == word[0]:
                    if helper(i,j,""):
                        return True
        return False