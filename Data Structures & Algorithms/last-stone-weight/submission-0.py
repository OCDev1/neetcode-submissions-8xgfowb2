class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = stones
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]  # for the max heap
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            s1 = heapq.heappop(maxHeap)
            s2 = heapq.heappop(maxHeap)
            newS = -1 * abs(s2 - s1)    # smash stones
            if newS:
                heapq.heappush(maxHeap, newS)    # if not 0 then put new stone back in heap
        
        # return final stone or 0
        if len(maxHeap):
            res = heapq.heappop(maxHeap)
            return abs(res)
        return 0