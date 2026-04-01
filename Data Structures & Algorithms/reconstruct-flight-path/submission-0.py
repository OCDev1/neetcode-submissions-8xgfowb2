class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # create adjacencey list to represent graph
        edge_map = defaultdict(list)
        tickets.sort()  # so we have lexicographic order
        tickets.reverse()   # reverse beacuse we pop from the right of the list
        for ticket in tickets:
            edge_map[ticket[0]].append(ticket[1])

        res = []    # final result

        def dfs(node):
            while edge_map[node]:   # recurse for all dest in city's list
                dest = edge_map[node].pop()
                dfs(dest)   # recurse for next dest
            res.append(node)    # after visiting all dests from city, add current city to res and return
        
        dfs('JFK')  # we always start from JFK

        return res[::-1]    # reverse order beacuse first airport gets added last