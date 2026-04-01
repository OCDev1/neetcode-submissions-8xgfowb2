class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edge_map = defaultdict(list)
        for src,dest,cost in times:
            edge_map[src].append((cost, dest))
        
        res = 0
        visited = set()
        minHeap = [(0,k)]

        while minHeap:
            cost1, node1 = heapq.heappop(minHeap)
            if node1 in visited:
                continue
            visited.add(node1)
            res = cost1

            for cost2, node2 in edge_map[node1]:
                if node2 in visited:
                    continue
                heapq.heappush(minHeap, (cost1 + cost2, node2))
        
        return -1 if len(visited) != n else res
