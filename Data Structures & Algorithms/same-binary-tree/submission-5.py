# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arrP = []
        arrQ = []

        # prints in order search to array
        def inOrder(root: Optional[TreeNode], arr: List[int]) -> None:
            if not root:
                arr.append(-101)
                return
            
            arr.append(root.val)
            inOrder(root.left, arr)
            inOrder(root.right, arr)
        
        inOrder(p, arrP)
        inOrder(q, arrQ)

        print(arrQ, arrP)
        return arrP == arrQ