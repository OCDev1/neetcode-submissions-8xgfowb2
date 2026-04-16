# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(root_p,root_q) -> bool:
            if not root_p and not root_q:
                return True
            if not(root_p) and root_q:
                return False
            if root_p and not(root_q):
                return False

            if root_p.val == root_q.val:
                return dfs(root_p.left,root_q.left) and dfs(root_p.right, root_q.right)
            else:
                return False
        return dfs(p,q)