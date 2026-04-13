class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)

        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        
        seen = set()

        def dfs(node):
            if node in seen:
                return
            seen.add(node)

            for nei in adjList[node]:
                if nei in seen:
                    continue
                dfs(nei)
            return
        ans = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                ans+=1
        return ans