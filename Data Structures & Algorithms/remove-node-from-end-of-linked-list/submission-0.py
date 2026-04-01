# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = head
        size = 1
        
        # find list size
        while head.next is not None:
            size += 1
            head=head.next
        head = res
        prev = None

        # reaching correct node
        for i in range(size-n):
            prev = head
            head = head.next
        # the removal itself
        if prev:
            prev.next = head.next
        else:   # when removing first node
            return head.next

        return res