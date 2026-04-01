class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.res = 0
        rows = len(grid)
        cols = len(grid[0])


        def helper(i,j):
            if (i >= rows or i < 0 or j >= cols or j < 0 or grid[i][j] == "0" or grid[i][j] == "#"):
                return

            grid[i][j] = "#"   # mark as visited

            # recurse
            helper(i + 1, j)
            helper(i - 1, j)
            helper(i, j + 1)
            helper(i, j - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    helper(i,j)
                    self.res += 1

        
        return self.res