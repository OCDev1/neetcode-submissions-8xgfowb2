class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        edge_map = { i : [] for i in range(n + 1) }
        for edge in edges:
            edge_map[edge[0]].append(edge[1])
            edge_map[edge[1]].append(edge[0])

        cycle = set()
        visited = set()
        cycle_start = -1

        def dfs(node, prev):
            nonlocal cycle_start    # declare nonlocal so global cycle_start is used
            if node in visited:   # if we found a cycle
                cycle_start = node  # mark as start of cycle
                return True
            
            visited.add(node)    # mark as visited

            # recursion
            for child in edge_map[node]:
                if child == prev:   # avoid false detection
                    continue
                if dfs(child, node):    # if path leads to cycle
                    if cycle_start != -1:   # not at start of cycle yet, add node to cycle set
                        cycle.add(node)
                    if cycle_start == node: # base case-we came back to start of cycle
                        cycle_start = -1
                    return True     # return that there is a cycle on the path
            return False    # no neighbor leads to a cycle
        
        dfs(1, -1)
        for u,v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]
