class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []

        def dfs(i):
            if sum(comb) == target and i >= len(nums):  # if we reached leaf of recursion tree and it equals target
                res.append(comb.copy()) # add current combo to res
            
            if i >= len(nums):  # if we reached leaf of recursion tree and its sum is not our target
                return  # return
            
            if sum(comb) > target:  # if we went over the target stop early
                return

            else:
                comb.append(nums[i])    # try adding current num
                dfs(i)  # check recursion with this decision
                comb.pop()  # try without adding current num
                dfs(i+1)  # check recursion with this decision
        
        dfs(0)
        return res