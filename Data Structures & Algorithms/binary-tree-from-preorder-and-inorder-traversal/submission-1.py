# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: index for index, val in enumerate(inorder)}
        
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        m = indices[root.val]
        
        # left subtree
        root.left = self.buildTree(preorder[1:], inorder[:m]) 
        # right subtree
        root.right = self.buildTree(preorder[m+1:], inorder[m+1:])
        return root
