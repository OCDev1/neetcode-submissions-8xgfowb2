class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r: int,c: int):
            if not(0 <= r < rows and 0 <= c < cols) or grid[r][c] == 0:
                return 0
            
            area = 0
            if grid[r][c] == 1:
                grid[r][c] = 0    # mark as visited
                for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:   # visit neighbors
                   area = area + dfs(r+dr,c+dc)
            return 1+area 
                
        
        # run check
        for r in range(rows):
            for c in range(cols):
                ans = max(dfs(r,c), ans)    # record max area

        return ans        