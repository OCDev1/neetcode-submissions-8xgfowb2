class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # We need to detect a cycle and remove an edge in the cycle
        # if we detect it in node x we remove an edge that touches node x
        # build adjacency list
        adjList = defaultdict(list)
        seen = set()
        
        def dfs(node: int,parent: int):
            if node in seen:
                return True
            
            seen.add(node)

            for nei in adjList[node]:
                if nei == parent:
                    continue
                if dfs(nei,node):
                    return True
            return False

        # every iteration we add an edge and run the check starting with that edge
        # if true - the last edge caused the cycle
        # undirected - edges go both ways
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
            seen = set()
            if dfs(a,-1):
                return [a,b]