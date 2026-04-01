class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to its prerequisites, for easier traversal of the graph
        prereq = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # save all visited nodes in current path
        visited = set()

        # search for cycle
        def dfs(course):
            if course in visited:   # detected cycle
                return False
            if prereq[course] == []:    # reached end of path (so no cycle here)
                return True
            
            visited.add(course)     # mark as visited

            # recurse for all children of current node
            for req in prereq[course]:  # for all edges leaving current node
                if not dfs(req):    # if one returns False then there is a cycle and we return False
                    return False

            visited.remove(course)
            prereq[course] = []     # this saves going down this path again later-we know this course is ok (no cycle).
            return True

        # check that all courses are doable
        for c in range(numCourses):
            if not dfs(c):
                return False    # cycle found, cant do this course so False
        return True


