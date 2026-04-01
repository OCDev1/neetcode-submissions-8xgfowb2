# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)  # dummy node
        carry = 0
        i = 0
        cur = head
        # sum the 2 digits
        while l1 or l2 or carry:
            # check values of nodes and assign them
            if l1:
                v1 = l1.val
            else:
                v1 = 0
            if l2:
                v2 = l2.val
            else:
                v2 = 0
            
            new_val = v1 + v2 + carry   # get sum
            carry = new_val // 10   # remember the carry
            cur.next = ListNode(int(new_val % 10))  # assign value to new node

            # update pointers
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            cur = cur.next
        
        return head.next






