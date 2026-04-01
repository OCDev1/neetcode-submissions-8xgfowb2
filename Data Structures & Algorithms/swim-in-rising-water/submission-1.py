class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        minHeap = [[grid[0][0], 0, 0]]  # minheap always gives us the cell with lowest value
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visited.add((0, 0))   # mark start as visited
        while minHeap:
            t, r, c = heapq.heappop(minHeap)    # pop next cell from minHeap
            if r == n - 1 and c == n - 1:   # if we reached the end return the time
                return t
            
            # explore all adjacent directions
            for dr, dc in directions:
                nextR, nextC = r + dr, c + dc
                # if out of bounds or already visited-skip
                if (nextR < 0 or nextC < 0 or nextR == n or nextC == n or (nextR, nextC) in visited):
                    continue
                visited.add((nextR, nextC)) # mark current as visited
                heapq.heappush(minHeap, [max(t, grid[nextR][nextC]), nextR, nextC]) # push the updated height to the minHeap