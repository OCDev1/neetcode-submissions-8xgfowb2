# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # flag
        balanced = True

        # function to check depth of tree
        def depthOfSub(root) -> int:
            nonlocal balanced
            if not root:
                return 0
            depthL,depthR = depthOfSub(root.left), depthOfSub(root.right)
            balanced = balanced and abs(depthL - depthR) <= 1   # if balanced is False at any point it stays False
            return max(depthL, depthR) + 1

        depthOfSub(root)
        return balanced

        