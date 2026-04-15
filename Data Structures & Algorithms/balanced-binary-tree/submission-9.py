# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True

        def dfs(node) -> int:
            nonlocal ans
            if not node:
                return 0
            leftDep = dfs(node.left)
            rightDep = dfs(node.right)
            if not (-1 <= rightDep-leftDep <= 1):
                ans = False
            return 1 + max(leftDep, rightDep)
        dfs(root)
        return ans