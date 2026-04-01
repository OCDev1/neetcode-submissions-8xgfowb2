class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edge_map = { i : [] for i in range(n)}  # set up map
        for a,b in edges:
            edge_map[a].append(b)
            edge_map[b].append(a)   # because it's an undirected graph
        
        visited = set()

        def dfs(node,prev):
            if node in visited:     # we already checked here and this node isn't in a cycle
                return False
            
            visited.add(node)   # mark as visited

            for child in edge_map[node]:    # continue the check for children
                if child != prev:     # we check both cases because it's undirected edges
                    if not dfs(child, node):  
                        return False    # child is in a cycle-return false
            return True
        
        if not dfs(0, -1):  # if there is a cycle-false
            return False
        if len(visited) != n:   # graph needs to be connected to be a tree so make sure we visited all nodes
            return False
        return True
            
            