class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # run bfs from all treasure cells
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        q = deque()

        # add first layer to queue (treasure cells)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))

        def bfs():
            dist = 0
            while q:
                level_size = len(q)
                for i in range(level_size): # assign dist to cells in cur layer
                    r,c = q.popleft()
                    
                    if (r,c) in seen or grid[r][c] == -1:
                        continue    # skip seen and skip water
                    
                    seen.add((r,c)) # mark as seen
                
                    grid[r][c] = min(grid[r][c], dist)  # record min distance

                    # traverse to neighbors
                    for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                        if 0 <= r+dr < rows and 0 <= c+dc < cols:
                            q.append((r+dr,c+dc))
                dist += 1
            return
        bfs()
        return