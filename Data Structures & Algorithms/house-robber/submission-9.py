class Solution:
    def rob(self, nums: List[int]) -> int:
        # f(n) = max(f(nums[n-1]), nums[n] + f(nums[n-2]))
        # max between not robbing and the max val up to house i-1 or robbing + max val up to house i-2
        # using dp:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        arr = [0] * (len(nums))

        arr[0] = nums[0]
        arr[1] = max(nums[1],arr[0])

        for i in range(2,len(nums)):
            arr[i] = max(arr[i-1], (nums[i] + arr[i-2]))
        return arr[-1]