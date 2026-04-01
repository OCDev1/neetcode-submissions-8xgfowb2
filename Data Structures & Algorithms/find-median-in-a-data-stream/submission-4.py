class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        # if new num is greater than min of large nums put it in minHeap
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            # if new num is greater than max of small nums put it in maxHeap
            heapq.heappush(self.maxHeap, -1 * num)
        
        # "balance" min and max heap so they are at most 1 different in size
        if self.minHeap and len(self.minHeap) > len(self.maxHeap) + 1:  # move from minH to maxH
            temp = heapq.heappop(self.minHeap)
            temp = temp * -1
            heapq.heappush(self.maxHeap, temp)

        if self.maxHeap and len(self.maxHeap) > len(self.minHeap) + 1:  # move from maxH to minH
            temp = heapq.heappop(self.maxHeap)
            temp = temp * -1
            heapq.heappush(self.minHeap, temp)

    def findMedian(self) -> float:
        # if they are not the same size take the head of larger one
        if (len(self.maxHeap) > len(self.minHeap)):
            maxtop = (self.maxHeap[0] * -1)
            return maxtop
        elif (len(self.maxHeap) < len(self.minHeap)):
            mintop = self.minHeap[0]
            return mintop
        # if they are the same size take average of the heads
        else:
            maxtop = (self.maxHeap[0] * -1)
            mintop = self.minHeap[0]
            return (mintop + maxtop) / 2
        
        