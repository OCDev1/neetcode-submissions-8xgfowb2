class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = [1] * len(nums)
        
        for i in range(1,len(nums)):
            for j in range(i):  # compare with all previous values until i
                if nums[i] > nums[j]:   # if nums[i] can extend the streak ending with nums[j]
                    arr[i] = max(arr[j] + 1, arr[i])    # max(adding nums[i] to nums[j]'s streak or skipping)

        return max(arr) # return the longest streak recorded