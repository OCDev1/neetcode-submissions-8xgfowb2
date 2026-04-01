# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)

        def findMin(lists) -> int:    # return the index of array cell with smallest value
            min_val = 1001
            res = -1
            for i in range(len(lists)):
                if lists[i] and lists[i].val < min_val:
                    min_val = lists[i].val
                    res = i
            return res      # if returns -1 then no more nodes
        head = dummy
        while findMin(lists) >= 0:
            head.next = lists[findMin(lists)]   # adding smallest node to list
            lists[findMin(lists)] = lists[findMin(lists)].next  # update list
            head = head.next
        return dummy.next
    