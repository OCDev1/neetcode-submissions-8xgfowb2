class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # courses and prerequisites form a graph - if there is a cycle: return false
        seen = set()
        safe = set()

        # for the traversal
        adjList = defaultdict(list)
        for prereq,course in prerequisites:
            adjList[course].append(prereq)

        def dfs(course):
            if course in safe:
                return True
            if course in seen:
                return False
            seen.add(course)

            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False
            seen.remove(course)
            safe.add(course)
            return True
            
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True