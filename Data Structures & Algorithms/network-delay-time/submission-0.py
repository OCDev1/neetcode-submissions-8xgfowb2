class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # creating adjacency list
        edge_map = defaultdict(list)
        for src,dest,cost in times:
            edge_map[src].append([cost,dest])
        
        visited = set()
        res = 0
        minHeap = [(0,k)]

        
        while minHeap:
            weight1, node1 = heapq.heappop(minHeap)
            if node1 in visited:
                continue    # avoid cycles

            visited.add(node1)  # mark as visited
            res = weight1

            for weight2, node2 in edge_map[node1]:  # for all neighbors of node1 (current node)
                if node2 not in visited:
                    heapq.heappush(minHeap, (weight1 + weight2, node2))     # add neighbor to queue with updated weight-weight of path up to node 2
       
        if len(visited) != n:
            return -1
        return res