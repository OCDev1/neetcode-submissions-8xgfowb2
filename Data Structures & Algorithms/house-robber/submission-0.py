class Solution:
    def rob(self, nums: List[int]) -> int:
        arr = [0] * (len(nums) + 2) # forst 2 cells are 0 -  base case

        for i in range(2, len(arr)):
            arr[i] = max(arr[i-1], arr[i-2] + nums[i-2])
        
        return arr[-1]