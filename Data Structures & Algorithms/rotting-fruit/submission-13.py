class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # This is the multi-source BFS pattern.
        # Plan: We add all rotting fruit to the queue then if any neighbors
        # are >0 we add to the q and after every bfs level we do +=1
        # to rot them.
        # The answer is the amount of BFS iterations we did.
        rows,cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        time = 0

        # add all rotting fruit cells to the queue
        # also count fresh fruit
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        
        def valid(r: int,c: int) -> bool:
            if 0 <= r < rows and 0 <= c <cols and grid[r][c] == 1:
                return True
            else:
                return False

        while fresh and q:
            level_size = len(q)

            for _ in range(level_size):
                r,c = q.popleft()
                
                # add neighbors
                for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr,nc = r+dr, c+dc
                    if valid(nr,nc):
                        # first mark then append
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
            time+=1

        if not fresh:
            return time
        else:
            return -1