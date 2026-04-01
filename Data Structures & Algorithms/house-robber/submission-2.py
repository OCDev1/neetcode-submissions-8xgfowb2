class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0 # save last 2 values (they're the only ones we need each iteration)

        for i in range(len(nums)):
            temp = max(two, one + nums[i])
            one = two
            two = temp
        
        return max(one, two)