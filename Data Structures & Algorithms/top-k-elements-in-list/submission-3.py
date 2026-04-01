class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        print(counter)

        # use a max heap to get k most frequent
        max_heap = []
        for key in counter:
            max_heap.append((-1 * counter[key],key))
        heapq.heapify(max_heap)

        ans = []

        for i in range(k):
            pair = heapq.heappop(max_heap)
            ans.append(pair[1])
        return ans
        