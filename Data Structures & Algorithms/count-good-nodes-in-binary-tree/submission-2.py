# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = 0

        def dfs(node, maxVal):
            nonlocal goodNodes
            if not node:
                return
            if node.val >= maxVal:
                goodNodes += 1
                dfs(node.left, node.val)
                dfs(node.right,node.val)
            else:
                dfs(node.left, maxVal)
                dfs(node.right,maxVal)
            return
        
        dfs(root, float('-inf'))
        return goodNodes