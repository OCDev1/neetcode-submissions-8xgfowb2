class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False    # can't reach cell i so game over
            max_reach = max(max_reach, i + nums[i])
        return True