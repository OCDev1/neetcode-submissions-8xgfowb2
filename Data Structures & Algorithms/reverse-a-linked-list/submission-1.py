# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        prev = head
        next_node = head.next
        next_next_node = head.next.next

        head.next = None

        while next_next_node:
            next_node.next = prev
            prev = next_node
            next_node = next_next_node
            next_next_node = next_next_node.next
        
        next_node.next = prev

        return next_node