class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(nums: List[int], index: int):
            if index == len(nums):  # we rached end of nums array
                res.append(nums.copy()) # add current permutation
                return
            
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index] # switch cur index with i
                backtrack(nums, index + 1)   # explore this option
                nums[index], nums[i] = nums[i], nums[index] # switch back for next iteration
        
        backtrack(nums, 0)
        return res