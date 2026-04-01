class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        # using hashmap to quickly find node of key
        self.key_to_node = {}
        self.capacity = capacity
        self.size = 0

        # Dummy head and tail to avoid checking for None
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node

    def _add(self, node):
        prev_last = self.tail.prev
        prev_last.next = node
        node.prev = prev_last
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        # Move accessed node to the end (most recently used)
        node = self.key_to_node[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            # Update existing node and move to end
            node = self.key_to_node[key]
            node.val = value
            self._remove(node)
            self._add(node)
        else:
            if self.size == self.capacity:
                # Remove least recently used node
                lru = self.head.next
                self._remove(lru)
                del self.key_to_node[lru.key]
                self.size -= 1
            # Add new node
            new_node = Node(key, value)
            self.key_to_node[key] = new_node
            self._add(new_node)
            self.size += 1





