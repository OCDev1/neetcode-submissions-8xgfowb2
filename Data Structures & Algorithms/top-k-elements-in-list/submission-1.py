class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        count = list(count.items())
        count.sort(key = lambda x:x[1])
        count.reverse()

        res=[]

        for i in range(k):
            res.append(count[i][0])
        return res    
        