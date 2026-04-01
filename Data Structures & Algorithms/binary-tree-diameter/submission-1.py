# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diam = 0

        # find depth of subtree
        def depthOfSub(root:Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            # get depth of left, right subtrees
            depthR = depthOfSub(root.right)
            depthL = depthOfSub(root.left)

            # update max diamter
            self.diam = max(depthR+depthL, self.diam)

            # return depth of current node
            return 1 + max(depthR,depthL)
        
        depthOfSub(root)
        return self.diam

        

