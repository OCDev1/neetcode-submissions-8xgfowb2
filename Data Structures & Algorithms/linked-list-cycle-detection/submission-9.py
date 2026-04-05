# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Rabbit and Hare
        slow,fast = head,head

        while fast and fast.next:   # If there is no cycle, fast will reach none before slow does
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False