class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = collections.deque()
        fresh = 0
        time = 0

        # count fresh so we know when to stop, add rotten to q so we know where to start
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    # add to queue
                    q.append((i,j))

        # run the bfs
        while fresh > 0 and q:
            qlen = len(q)
            for i in range(qlen):   # do current layer of bfs
                r, c = q.popleft()

                # search vertical and horizontal neighbors 
                for dr, dc in [[1,0],[-1,0],[0,-1],[0,1]]:
                    row, col = r + dr, c + dc
                    
                    # if we found fresh fruit, rot it and add to queue
                    if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1

        if fresh == 0:
            return time
        else:
            return -1


            


