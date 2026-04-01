# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        self.bfs(root, 0, res)

        return res

    def bfs(self, root: Optional[TreeNode], level: int, res: List[List[int]])-> None:
        if not root:
            return
        if len(res) <= level:
            res.append([])
        res[level].append(root.val)
        self.bfs(root.left,level+1 , res)
        self.bfs(root.right,level+1 , res)
        return
