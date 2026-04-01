class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        cur_set = []

        def helper(i):
            if i >= len(nums):
                res.append(cur_set.copy())
                return
            cur_set.append(nums[i])
            helper(i+1)
            cur_set.pop()
            
            # this helps us avoid duplicate sets by skipping all instances of current number
            while i < len(nums) - 1 and nums[i] == nums[i+1]:   # move until we reach new number
                i += 1
            helper(i+1) # explore path without the current number
        helper(0)
        return res