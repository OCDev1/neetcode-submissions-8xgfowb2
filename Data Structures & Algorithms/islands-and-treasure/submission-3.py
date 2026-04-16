class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # we add all treasure coords to the bfs queue, count bfs iterations
        # each cell we reach we update its value and add its neighbors if
        # they can be reached
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        count = 0
        seen = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    seen.add((r,c))
        
        while q:
            level_size = len(q)

            for _ in range(level_size):
                r,c = q.popleft()
                grid[r][c] = min(count, grid[r][c])
                for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr,nc = r+dr,c+dc
                    if ((nr,nc) not in seen and
                     (0<=nr<rows) and
                     (0<=nc<cols) and 
                     grid[nr][nc] > 0):    # cant go through -1 (water)
                        q.append((nr,nc))
                    seen.add((r,c))
            count += 1




