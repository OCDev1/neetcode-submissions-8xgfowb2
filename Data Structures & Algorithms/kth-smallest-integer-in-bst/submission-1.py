# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def in_order(root: Optional[TreeNode]) -> None:
            if root.left:
                in_order(root.left)

            arr.append(root.val)

            if root.right:
                in_order(root.right)    
        
        in_order(root)
        print(arr)
        return arr[k-1]

