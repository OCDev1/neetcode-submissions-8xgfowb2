class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur_list = []
        
        def dfs(i):
            if i == len(nums):
                ans.append(cur_list.copy())
                return
            dfs(i+1)
            cur_list.append(nums[i])
            dfs(i+1)
            cur_list.pop()
        
        dfs(0)
        return ans