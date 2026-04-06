# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS and record last node in every level
        if not root:
            return []
        ans = []
        q = collections.deque()
        q.append(root)
        while q:
            levelSize = len(q)
            for i in range(levelSize):
                node = q.popleft()
                if i == (levelSize - 1):
                    ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans