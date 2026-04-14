class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # The array is basically an adjacency list
        # The underlying pattern is cycle detection in a directed graph
        # We can run DFS from each node and if we see a node already seen
        # then we found a cycle
        adjList = defaultdict(list)

        # populate adjList
        for crs,prereq in prerequisites:
            adjList[crs].append(prereq)
        
        seen = set()
        safe = set()    # optimization to save time on paths we already checked

        def dfs(node: int) -> bool:
            if node in seen:
                return False
            if node in safe:
                return True
            
            seen.add(node)  # mark as seen
            for nei in adjList[node]:
                if not dfs(nei):
                    return False
            seen.remove(node)   # backtrack
            safe.add(node)  # we came back from recursion - no cycle == safe
            return True

        # run dfs from all nodes
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True