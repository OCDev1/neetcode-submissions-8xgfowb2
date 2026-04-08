class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        highest = curSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, num + curSum)
            highest = max(highest, curSum)
        return highest