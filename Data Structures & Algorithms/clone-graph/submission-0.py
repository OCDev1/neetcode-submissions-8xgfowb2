"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}
        res = node

        def helper(node):
            if node in old_to_new:
                return old_to_new[node]

            copy = Node(node.val)
            old_to_new[node] = copy
            for neighbor in node.neighbors:
                old_to_new[node].neighbors.append(helper(neighbor)) # add neighbors to node's list
            return copy
        
        if node:
            helper(node)
        else:
            return None
        return old_to_new[node]