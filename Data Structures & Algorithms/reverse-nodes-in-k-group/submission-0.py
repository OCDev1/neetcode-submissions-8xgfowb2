# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        count = 0

        while cur and count < k:
            cur = cur.next
            count += 1

        if count == k:  # if less than k remain we return the list as is
            cur = self.reverseKGroup(cur, k)    # recursively reverse the list starting from last of current list to kth after
            # reverse current list
            while count > 0:
                tmp = head.next     # saving the next node
                head.next = cur     # reversing the link
                cur = head          # moving forward
                head = tmp          # saving the next node
                count -= 1
            head = cur              # new head of the reversed list
        return head
