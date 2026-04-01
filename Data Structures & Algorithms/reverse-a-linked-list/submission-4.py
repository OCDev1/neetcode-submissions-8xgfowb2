# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,cur = None, head

        while cur:
            temp = cur.next # save rest of list
            cur.next = prev # make the flip
            prev = cur  # move forward
            cur = temp  # move forward
        return prev