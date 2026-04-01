# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        in_order = []

        # scan in order
        def inOrder(root: Optional[TreeNode]) -> None:
            if not root:
                return
            inOrder(root.left)
            in_order.append(root.val)
            inOrder(root.right)
            return

        inOrder(root)

        # check sorted
        for i in range(len(in_order)-1):
            if in_order[i] < in_order[i+1]:
                continue
            else:
                return False
        return True