# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # use slow,fast pointers
        slow = fast = head
        index = -1
        count = -1
        while fast:
            count += 1
            fast = fast.next
            if count % 2:
                slow = slow.next
            if fast == slow:
                index = count
                break
        if index == -1:
            return False
        return True