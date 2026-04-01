# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are null, they're the same
        if not p and not q:
            return True
        
        # If one is null and the other is not, they're not the same
        if not p or not q:
            return False

        # If the values differ, they're not the same
        if p.val != q.val:
            return False
        
        # recursion
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)


