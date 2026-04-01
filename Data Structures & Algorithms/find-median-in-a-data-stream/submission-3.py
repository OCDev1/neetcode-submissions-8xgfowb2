class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -1 * num)
        
        # "balance" min and max heap
        if self.minHeap and len(self.minHeap) > len(self.maxHeap) + 1:
            temp = heapq.heappop(self.minHeap)
            temp = temp * -1
            heapq.heappush(self.maxHeap, temp)

        if self.maxHeap and len(self.maxHeap) > len(self.minHeap) + 1:
            temp = heapq.heappop(self.maxHeap)
            temp = temp * -1
            heapq.heappush(self.minHeap, temp)
        
        print(self.minHeap)
        print(self.maxHeap)

    def findMedian(self) -> float:
        if (len(self.maxHeap) > len(self.minHeap)):
            maxtop = (self.maxHeap[0] * -1)
            return maxtop
        elif (len(self.maxHeap) < len(self.minHeap)):
            mintop = self.minHeap[0]
            return mintop 
        else:
            maxtop = (self.maxHeap[0] * -1)
            mintop = self.minHeap[0]
            return (mintop + maxtop) / 2
        
        