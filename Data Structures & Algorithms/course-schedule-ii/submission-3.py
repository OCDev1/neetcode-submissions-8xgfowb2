class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # mapping course to its prerequisites
        prereq_map = {i : [] for i in range(numCourses)}
        for crs in prerequisites:
            prereq_map[crs[0]].append(crs[1])
        
        visited = set() # so we dont append same course twice
        cycle = set()   # so we can detect cycle 
        res = []

        def dfs(crs):
            if crs in cycle:    # there is a cycle, cant complete courses
                return False
            if crs in visited:   # already checked this course
                return True

            # if we made it here we arent at end of path yet
            cycle.add(crs)  # add to cycle detection
            # recurse for all prereqs
            for prereq in prereq_map[crs]:
                if not dfs(prereq):
                    return False

            cycle.remove(crs)   # remove for future path checks
            visited.add(crs)    # add current course to visited
            res.append(crs)     # add current course to result
            return True
        
        # go over all courses
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
