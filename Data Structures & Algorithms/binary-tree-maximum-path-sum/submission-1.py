# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # global variable for result
        self.res = -1000001

        def maxVal(root: Optional[TreeNode]) -> int:
            # edge case
            if not root:
                return 0

            # recursive calls
            left = max(0, maxVal(root.left))    # return max between pursuing or not pursuing this path to the left
            right = max(0, maxVal(root.right))  # same for right

            # maintain max path sum variable
            self.res = max(self.res, (root.val + left + right)) 
            
            # return the max path sum achievable from this node
            return root.val + max(left, right)  
            
        maxVal(root)
        return self.res
