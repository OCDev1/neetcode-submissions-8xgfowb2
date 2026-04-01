class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        INF = 2147483647

        for i in range(ROWS):
            for j in range(COLS):
                # start searches from the gates
                if grid[i][j] == 0:
                    q.append((i,j,0))

        while q:
            i,j,dist = q.popleft()

            # check 4 adjacent cells
            for r,c in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
                if (0 <= r < ROWS and 0 <= c < COLS and grid[r][c] != -1 and grid[r][c] != 0 and grid[r][c] > dist):
                    grid[r][c] = dist + 1   # change value
                    q.append((r,c,dist + 1))    # add to search queue