class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = nums
        heapq.heapify(self.minheap) # heapify is O(n)
        while len(self.minheap) > self.k:   # gets rid of all but k largest elements
            heapq.heappop(self.minheap)  # kth largest is at top

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)   # add new value to heap
        if len(self.minheap) > self.k:   # maintain k largest elements in heap
            heapq.heappop(self.minheap)
        return self.minheap[0]  # return head
