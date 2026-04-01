"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        old_to_new_address_map = {}  # old node address -> new node address

        # create a copy of the list without randoms yet.
        old_pointer = head
        new_head = new_pointer = Node(0, None, None)
        while old_pointer:
            # copy vals from old list to new list
            new_pointer.val = old_pointer.val
            new_pointer.next = Node(0, None, None)
            new_pointer.random = None   # for now
            # update our hash map
            old_to_new_address_map[old_pointer] = new_pointer
            if not old_pointer.next:    # end of new list
                new_pointer.next = None
            # move onwards
            old_pointer = old_pointer.next
            new_pointer = new_pointer.next

        # update random pointers in new list
        p_old = head
        p_new = new_head
        while p_old:
            if p_old.random:    # if the random is not null
                old_random = p_old.random  # get the address of the random
                p_new.random = old_to_new_address_map[old_random]  # connect the random node by looking up its address on the hashmap
            else:
                p_new.random = None # if the random is null
            p_old = p_old.next
            p_new = p_new.next
        return new_head

