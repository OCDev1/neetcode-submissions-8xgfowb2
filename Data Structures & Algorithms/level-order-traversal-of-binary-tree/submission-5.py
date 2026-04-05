# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Do BFS
        if not root:
            return []
        q = collections.deque()
        q.append(root)

        res = []
        while q:
            qLen = len(q)
            curlvl = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    curlvl.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if curlvl:
                res.append(curlvl)
        return res