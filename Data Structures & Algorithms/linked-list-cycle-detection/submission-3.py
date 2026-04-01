#
# O(n) time O(1) space
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # use slow,fast pointers
        slow = fast = head
        index = -1  # start of cycle
        count = -1  # iteration number
        while fast:
            count += 1
            fast = fast.next  # always move fast pointer
            if count % 2:  # move slow pointer every other iteration
                slow = slow.next
            if fast == slow:    # if slow and fast are pointing to the same node
                index = count   # save the index of the start of the cycle and break
                break
        if index == -1:  # there was no cycle
            return False
        return True