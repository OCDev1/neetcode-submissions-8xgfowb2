# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        my_map = {} # for easier creation of new list
        carry = 0
        i = 0
        # sum the 2 digits
        while l1 or l2 or carry:
            new_node = ListNode(0)  # init new node
            new_val = 0
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
            new_node.val = int(new_val % 10)  # assign value to new node
            my_map[i] = new_node    # add node to mapping
            i += 1

            # update pointers
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        my_map[i] = None
        
        print(my_map)

        # creating new list via hashmap:
        for i in range(len(my_map)-1):
            my_map[i].next = my_map[i+1]
        return my_map[0]






