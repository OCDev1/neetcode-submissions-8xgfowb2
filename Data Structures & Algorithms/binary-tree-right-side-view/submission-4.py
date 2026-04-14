# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # We should run BFS which works in layers of depths
        # we will append and popleft from the queue so the right-most is the last in queue
        # in every level
        q = deque()
        ans = []
        if root: 
            q.append(root)
        while q:
            level_size = len(q)
            # process current level
            for _ in range(level_size-1):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            # process rightmost node:
            node = q.popleft()
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            # record its value
            ans.append(node.val)
        
        return ans