# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            print(q)
            for i in range(qLen-1):
                node = q.popleft()  # reach rightmost node in current level
                if node:

                    if node.left: q.append(node.left) # add it's children to queue
                    if node.right: q.append(node.right)
                else:
                    continue
            node = q.popleft()  # pop rightmost in current level
            if node:
                res.append(node.val)    # add its val to res
                if node.left: q.append(node.left) # add it's children to queue
                if node.right: q.append(node.right)
        return res


