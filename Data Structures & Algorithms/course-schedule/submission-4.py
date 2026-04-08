class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        # build adj list hash map for easier traversal
        # prereq = node, courses = neighbors list
        for (prereq, course) in prerequisites:
            adj[prereq].append(course)
        
        # seen = visited on current traversal
        seen = set()
        # safe = courses (nodes) with no cycles
        safe = set()

        def dfs(node):
            if node in seen:
                return False
            if node in safe:
                return True
            
            seen.add(node)
            for course in adj[node]:
                if not dfs(course):
                    return False
            seen.remove(node)
            safe.add(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True