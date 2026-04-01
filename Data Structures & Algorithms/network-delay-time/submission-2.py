class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # creating adjacency list
        edge_map = defaultdict(list)
        for src,dest,cost in times:
            edge_map[src].append((cost, dest))
        
        res = 0
        visited = set()     # to mark visited and avoid cycles
        minHeap = [(0,k)]   # init minHeap with source node

        while minHeap:
            cost1, node1 = heapq.heappop(minHeap)   # pop closest node
            if node1 in visited:    
                continue    # to avoid cycles check if already visited
            visited.add(node1)  # mark as visited
            res = cost1     # current res is the cost of node beacuse the cost of each node is the cost of the entire path leading to it

            for cost2, node2 in edge_map[node1]:    # for all neighbors of node1 (current node)
                if node2 in visited:
                    continue
                heapq.heappush(minHeap, (cost1 + cost2, node2)) # add neighbor to queue with updated weight-weight of path up to node 2
        
        return -1 if len(visited) != n else res
