class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            # if we are out of bounds or cant reach prevHeight from current cell, return
            if ((r, c) in visit or 
                r < 0 or c < 0 or 
                r == ROWS or c == COLS or 
                heights[r][c] < prevHeight  # prev cell cant be reached from this cell
            ):
                return
            
            # add cur cell to set of ocean we came from
            visit.add((r, c))

            # recursive calls
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            # run search from all cells touching pacific
            dfs(0, c, pac, heights[0][c])
            # run search from all cells touching atlantic
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                # if cell is in both pacific and atlantic sets, it can reach both and is in solution
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res