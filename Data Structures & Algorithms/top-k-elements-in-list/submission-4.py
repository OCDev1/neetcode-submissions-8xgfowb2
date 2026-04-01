class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        countList = list(count.items())

        countList.sort(key = lambda x: x[1]) # sort by frequency

        ans = []
        for i in range(k):
            most = countList.pop()[0]
            ans.append(most)
        return ans