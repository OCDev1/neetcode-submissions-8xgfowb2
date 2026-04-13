"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # we run dfs on the graph, if a node doesnt have a copy in oldToNew
        # we create one and add to oldToNew
        # we must copy the val and the neighbors (they should be copies too)
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]   # return the existing copy
            if not node:
                return
            
            copy = Node(node.val)
            oldToNew[node] = copy
            # deep copy the neighbors of the node
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            # return the copy
            return copy
        
        return dfs(node)