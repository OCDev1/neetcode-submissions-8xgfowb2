class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        maxHeap = []
        for key,value in count.items():
            value = value * -1
            maxHeap.append((value, key))
        heapq.heapify(maxHeap)
        ans = []
        for i in range(k):
            pair = heapq.heappop(maxHeap)
            most = pair[1]
            ans.append(most)
        return ans