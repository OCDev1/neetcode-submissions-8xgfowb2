# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        elif not list2: return list1
        # resHead = min(L1,L2)
        # advance pointer of min L1,L2
        if list1.val <= list2.val:
            resHead = list1
            list1 = list1.next
        else:
            resHead = list2
            list2 = list2.next
        res = resHead

        while list2 and list1:
            if list1.val <= list2.val:
                res.next = list1
                list1 = list1.next
            else:
                res.next = list2
                list2 = list2.next
            res = res.next
        res.next = list1 if list1 else list2
        return resHead