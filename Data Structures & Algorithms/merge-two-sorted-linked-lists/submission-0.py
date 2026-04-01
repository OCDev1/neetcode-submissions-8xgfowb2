# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = None  #pointer to head
        curr = None #pointer to current

        # empty list
        if not list1:
            return list2
        elif not list2:
            return list1

        # assigning the head of result
        if list1.val > list2.val:
            res = list2
            list2 = list2.next
            curr = res
        else:
            res = list1
            list1 = list1.next
            curr = res
        
        # ACTUAL MERGING
        while list1 != None and list2 != None:
            if list1.val > list2.val:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
            else:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
        
        if not list1 and not list2:
            return res

        elif not list1:
                curr.next = list2
        elif not list2:
                curr.next = list1

        return res
    


