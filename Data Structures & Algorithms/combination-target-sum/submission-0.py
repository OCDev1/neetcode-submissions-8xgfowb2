class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []

        def dfs(i):
            if sum(comb) == target and i >= len(nums):
                res.append(comb.copy())
            
            if i >= len(nums):
                return
            
            if sum(comb) > target:
                return
            else:
                comb.append(nums[i])
                dfs(i)
                comb.pop()
                dfs(i+1)
        
        dfs(0)
        return res