# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right) -> bool:
            if not node:
                return True
            # subtree with no children is already sorted
            if not (right > node.val > left):
                return False
            
            # recursion
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
        return valid(root, float("-inf"), float("inf"))