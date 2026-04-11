class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        seen = set()

        # tries to find word, starting from cell [r][c]
        def dfs(r,c,i):
            if i == len(word):
                return True
            if not(0 <= r < rows) or not(0 <= c < cols):
                return False
            if (r,c) in seen or board[r][c] != word[i]:
                return False
            
            seen.add((r,c)) # mark cell as seen on this attempt 
            
            # continue the search
            found = dfs(r-1,c,i+1) or dfs(r+1,c,i+1) or dfs(r,c-1,i+1) or dfs(r,c+1,i+1)
            
            # backtrack
            seen.remove((r,c))
            return found

        # start word search from every cell, it could contain the first letter
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False