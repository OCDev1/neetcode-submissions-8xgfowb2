class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # init
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        # dfs - if we see a 1 turn it to 0 to avoid duplication, then go to neighbors
        def dfs(r,c):
            if not (0 <= r < rows) or not (0 <= c < cols) or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'  # mark as seen
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        # go over the matrix, if we see a 1 - run dfs then increment count
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r,c)
                    islands += 1
        return islands