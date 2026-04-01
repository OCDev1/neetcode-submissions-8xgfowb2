# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        level = 0
        queue = collections.deque()
        queue.append(root)

        while queue:
            queue_len = len(queue)
            if len(res) == level:   # create new list for new level
                res.append([])
            for i in range(queue_len):  # do these actions only for nodes that are from previous iteration
                cur = queue.popleft()
                if cur:
                    res[level].append(cur.val)      # add cur val to proper list
                    queue.append(cur.left)      # add children to queue
                    queue.append(cur.right)
            level += 1

        res.pop()
        return res


