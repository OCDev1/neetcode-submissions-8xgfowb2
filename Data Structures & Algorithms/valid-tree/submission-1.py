class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edge_map = { i : [] for i in range(n)}  # set up map
        for a,b in edges:
            edge_map[a].append(b)
            edge_map[b].append(a)   # because it's an undirected graph
        
        cycle = set()
        visited = set()
        used_edges = set()

        def dfs(node):
            if node in cycle:   # we have a cycle-not a tree
                return False
            if node in visited:     # we already checked here and this node isn't in a cycle
                return True
            
            visited.add(node)   # mark as visited
            cycle.add(node)     # add for future cycle checks in this path

            for child in edge_map[node]:    # continue check for children
                if (node, child) not in used_edges and (child, node) not in used_edges:
                    used_edges.add((node,child))    # mark current edge as used
                    if not dfs(child):  
                        return False    # child is in a cycle-return false
                    cycle.remove(child)  # empty cycle set for the next path checks
            return True
        
        if not dfs(0):
            return False
        if len(visited) != n:   # graph needs to be connected to be a tree
            return False
        return True
            
            