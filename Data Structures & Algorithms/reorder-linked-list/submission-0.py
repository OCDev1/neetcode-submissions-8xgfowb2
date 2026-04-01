# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

        # splitting list into 2 lists
        slow, fast = head, head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        # slow.next is now the head of 2nd list
        head2 = slow.next
        slow.next = None

        #reversing second list
        prev = None       
        while head2:
            temp = head2.next
            head2.next = prev
            prev = head2
            head2 = temp
        
        #merge lists
        p1 = head
        p2 = prev
        cur = head
        while p2:
            tmp1,tmp2 = p1.next, p2.next
            p1.next = p2
            p2.next = tmp1
            p1, p2 = tmp1, tmp2
        




