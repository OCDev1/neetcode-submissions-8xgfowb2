class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        edge_map = {i: [] for i in range(n)}
        # calculate Manhattan distance between every 2 points and add to adj list
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edge_map[i].append([dist, j])
                edge_map[j].append([dist, i])
        
        visited = set()   # so we know what's already connected
        minHeap = [[0, 0]]  # start from node 0
        
        while len(visited) < n:
            cost, i = heapq.heappop(minHeap) # pop from heap
            if i in visited:
                continue    # we already have an edge to this point
            res += cost     # add distance to i to cost
            visited.add(i)  # mark i as visited

            for neighbour in edge_map[i]:
                if neighbour[1] not in visited:
                    heapq.heappush(minHeap, [neighbour[0],neighbour[1]])    # push i's neighbours to minHeap
        
        return res
        

