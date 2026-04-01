class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = nums
        heapq.heapify(self.minheap)
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)  # kth largest is at top

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:   # maintain k largest elements in heap
            heapq.heappop(self.minheap)
        return self.minheap[0]
