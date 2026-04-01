# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Serialize both trees
        root_str = self.serialize(root)
        subRoot_str = self.serialize(subRoot)
        
        # Check if subRoot's serialization is a substring of root's serialization
        return subRoot_str in root_str
    
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Serialize the tree using preorder traversal with markers for null nodes."""
        serialized = []
        
        def preorder(node):
            if not node:
                serialized.append("#")  # Marker for None
                return
            serialized.append(f",{node.val}")  # Add comma to separate nodes
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return "".join(serialized)
