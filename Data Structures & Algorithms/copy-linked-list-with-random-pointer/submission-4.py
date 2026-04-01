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
        old_to_new_address_map = {None:None}  # old node address -> new node address

        # populate hashmap
        old_pointer = head
        while old_pointer:
            new_pointer = Node(0, None, None)
            # update our hash map
            old_to_new_address_map[old_pointer] = new_pointer
            # move onwards
            old_pointer = old_pointer.next

        # copy vals from old list to new list
        p_old = head
        while p_old:
            p_new = old_to_new_address_map[p_old]
            p_new.val = p_old.val   # update val
            p_new.next = old_to_new_address_map[p_old.next]     # update next
            p_new.random = old_to_new_address_map[p_old.random]  # update random
            p_old = p_old.next
        return old_to_new_address_map[head]

