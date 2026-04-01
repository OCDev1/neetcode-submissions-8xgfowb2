# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        diam = 0
        
        left = self.depthOfSub(root.left) if root.left else 0
        right = self.depthOfSub(root.right) if root.right else 0
        diam = diam + left + right
        diamR = self.diameterOfBinaryTree(root.right) if root.right else 0
        diamL = self.diameterOfBinaryTree(root.left) if root.left else 0
        res = max(diam, diamR, diamL)

        return res

    # find depth of subtree
    def depthOfSub(self, root:Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        depthR = self.depthOfSub(root.right) if root.right else 0
        depthL = self.depthOfSub(root.left) if root.left else 0
        return 1 + max(depthR, depthL)

