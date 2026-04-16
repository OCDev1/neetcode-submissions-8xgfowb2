# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # map number to its index in inorder array for O(1) access
        inord_idx = defaultdict(int)
        for i in range(len(inorder)):
            inord_idx[inorder[i]] = i

        pre_idx = 0

        def dfs(l,r):
            nonlocal pre_idx
            if l>r:
                return None

            # construct root node
            node_val = preorder[pre_idx]
            node = TreeNode(node_val)
            pre_idx += 1

            m = inord_idx[node_val]

            # recurse to left and right subtree
            node.left = dfs(l, m-1)
            node.right = dfs(m+1, r)

            return node
        return dfs(0, len(inorder) - 1)