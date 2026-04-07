class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # we run dfs from pacific cells, run dfs from atlantic cells and check the intersection
        ans = []
        pacific = set()
        atlantic = set()
        rows = len(heights)
        cols = len(heights[0])

        def dfs(r,c,ocean):
            if (r,c) in ocean:
                return
            if not (0 <= r < rows) or not (0 <= c < cols):
                return
            
            ocean.add((r,c))
            
            for dr,dc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                if (0 <= dr < rows) and (0 <= dc < cols) and heights[dr][dc] >= heights[r][c]:
                    dfs(dr,dc,ocean)
        
        for c in range(cols):
            dfs(0,c,pacific)
        for r in range(rows):
            dfs(r,0,pacific)
        for r in range(rows):
            dfs(r,cols-1,atlantic)
        for c in range(cols):
            dfs(rows-1,c,atlantic)
        
        for coord in pacific:
            if coord in atlantic:
                ans.append(list(coord))
        return ans