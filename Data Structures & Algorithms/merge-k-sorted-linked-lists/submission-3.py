# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i in range(len(lists)):
            if not lists[i]:
                continue
            heap.append((lists[i].val, i,lists[i])) # (val, ptr, list index)
        heapq.heapify(heap)

        dummy = ListNode(-1)
        cur = dummy

        while heap:
            val, i, min_node = heapq.heappop(heap)
            # add min node to final list
            cur.next = min_node
            # move pointer in final list
            cur = cur.next

            # move ptr fwd in list[i] and push its new min value
            if min_node.next:
                heapq.heappush(heap, (min_node.next.val, i, min_node.next))
        return dummy.next