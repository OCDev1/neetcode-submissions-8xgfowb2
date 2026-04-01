# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2lists(list1: ListNode, list2: ListNode) -> Optional[ListNode]:
            # if theres only 1 list return it
            # Dummy node to help simplify code by avoiding special cases
            dummy = ListNode()
            current = dummy

            # Traverse both lists and add the smaller node to the new list
            while list1 and list2:
                if list1.val < list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next

            # Attach any remaining nodes in list1 or list2
            current.next = list1 if list1 else list2

            return dummy.next  # Return the merged list, starting at dummy.next
                    # merge the 2 and return head of merged list

        if len(lists) == 2:
            return merge2lists(lists[0],lists[1])
        elif len(lists) == 1:
            return lists[0]
        elif not len(lists):
            return None
        
        m = len(lists) // 2
        return merge2lists(self.mergeKLists(lists[:m]), self.mergeKLists(lists[m:]))

        