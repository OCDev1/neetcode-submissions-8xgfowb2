class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        def helper(i,j):
            if(i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j]==9 or grid[i][j]==0):
                return 0

            grid[i][j] = 9  # mark as visited

            # recurse
            return (1 + helper(i-1,j)+
            helper(i+1,j)+
            helper(i,j-1)+
            helper(i,j+1))
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    area = helper(i,j)
                    res = max(res,area)
        
        return res