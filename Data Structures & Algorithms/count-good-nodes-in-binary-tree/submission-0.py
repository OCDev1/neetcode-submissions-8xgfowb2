# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        max_val = -101

        def dfs(root, max_val) -> None:
            nonlocal res
            if not root:
                return
            max_val = max(max_val, root.val)
            if root.val >= max_val:
                res += 1
            dfs(root.left, max_val)
            dfs(root.right, max_val)
            return

        dfs(root, max_val)
        return res

             
