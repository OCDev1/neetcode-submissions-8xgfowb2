class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        ans = list(count.items())
        ans.sort(key = lambda x:x[1])
        ans.reverse()

        res=[]

        for i in range(k):
            res.append(ans[i][0])
        return res    
        