class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        index0 = [0] * (n + 1)
        index1 = [0] * (n + 2)

        for i in range(n - 1):
            index0[i + 2] = max(index0[i+1], index0[i] + nums[i]) 

        for i in range(1,n):
            index1[i + 2] = max(index1[i+1], index1[i] + nums[i])

        return max(index1[-1], index0[-1])