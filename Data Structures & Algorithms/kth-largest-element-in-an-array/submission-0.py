class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        # turn nums to negatives
        for num in nums:
            maxHeap.append(-1*num)

        heapq.heapify(maxHeap)

        while k > 0 :
            ans = heapq.heappop(maxHeap)
            k-=1

        return -1 * ans