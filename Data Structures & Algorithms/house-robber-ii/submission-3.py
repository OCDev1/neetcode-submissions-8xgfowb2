class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        index0 = [0] * (n + 1)
        index1 = [0] * (n + 2)

        one1,two1 = 0, 0
        one2,two2 = 0, 0

        for i in range(n - 1):
            temp1 = max(two1, one1 + nums[i])
            one1 = two1
            two1 = temp1  

        for i in range(1,n):
            temp2 = max(two2, one2 + nums[i])
            one2 = two2
            two2 = temp2 

        return max(two1, two2)