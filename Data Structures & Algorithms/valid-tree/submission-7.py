class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Tree == fully connected with no cycles
        adjList = defaultdict(list)

        for src,dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)    # undirected graph

        # We will run dfs marking seen nodes
        seen = set()

        def dfs(node,par):
            if node in seen:
                return False
            
            seen.add(node)
            for nei in adjList[node]:
                if nei == par:
                    continue
                if not dfs(nei,node):
                    return False
            return True

        return dfs(0,-1) and len(seen) == n