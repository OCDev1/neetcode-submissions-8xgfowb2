# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # function to check depth of tree
        def depthOfSub(root) -> int:
            if not root:
                return 0
            depthL,depthR = depthOfSub(root.left), depthOfSub(root.right)
            depth = 1 + max(depthL, depthR)
            return depth

        if not root:
            return True

        # check current node is balanced
        if abs(depthOfSub(root.left) - depthOfSub(root.right)) > 1:
            return False
        
        # recursive checks for left, right subtrees
        l = self.isBalanced(root.left)
        r = self.isBalanced(root.right)

        # return the verdict
        return l and r        

        