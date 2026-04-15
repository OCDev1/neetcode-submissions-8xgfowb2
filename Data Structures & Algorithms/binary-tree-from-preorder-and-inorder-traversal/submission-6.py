# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inordIndex = defaultdict(int)
        for i in range(len(inorder)):
            inordIndex[inorder[i]] = i
        pre_idx = 0

        def dfs(l,r):
            nonlocal pre_idx
            if l > r:
                return
            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)

            middle = inordIndex[root_val]

            root.left = dfs(l, middle - 1)
            root.right = dfs(middle + 1, r)
            return root
        return dfs(0,len(inorder) - 1)