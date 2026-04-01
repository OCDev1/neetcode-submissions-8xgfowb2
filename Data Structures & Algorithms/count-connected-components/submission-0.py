class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # adding edges to map
        edge_map = { i : [] for i in range(n)}
        for edge in edges:
            edge_map[edge[0]].append(edge[1])
            edge_map[edge[1]].append(edge[0])
        
        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            # recursive calls
            for child in edge_map[node]:
                dfs(child)
            return

        counter = 0
        for i in range(n):
            len_visited = len(visited)
            dfs(i)
            if len_visited != len(visited):
                counter += 1
        return counter
