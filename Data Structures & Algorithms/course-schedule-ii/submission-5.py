class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)

        # populate the adjList
        for crs, prereq in prerequisites:
            adjList[crs].append(prereq)

        safe = set()
        path = set()
        ans = []

        def dfs(node: int) -> bool:
            if node in path:    # cycle detected
                return False
            if node in safe:
                return True
            
            # add the node to the cur path
            path.add(node)
            # iterate over neighbors
            for nei in adjList[node]:
                if not dfs(nei):
                    return False
            # we came back - no cycles
            safe.add(node)
            # add to answer
            ans.append(node)
            # backtrack
            path.remove(node)
            return True
        
        # run dfs from all (nodes) courses
        for i in range(numCourses):
            if not dfs(i):
                return []
        return ans
        