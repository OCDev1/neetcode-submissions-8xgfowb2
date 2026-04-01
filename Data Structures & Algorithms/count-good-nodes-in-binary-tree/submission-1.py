# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        max_val = -101  # lowest possible value

        def dfs(root, max_val) -> None:
            nonlocal res    # global variable res
            if not root:
                return
            max_val = max(max_val, root.val)    # update max in path
            if root.val >= max_val:         # if this is a good node increment res
                res += 1
            dfs(root.left, max_val)     # recursive calls
            dfs(root.right, max_val)
            return

        dfs(root, max_val)
        return res

             
