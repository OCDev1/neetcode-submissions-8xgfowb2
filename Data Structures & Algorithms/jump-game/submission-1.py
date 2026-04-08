class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal: # can I reach the goal from prev step + it's value?
                goal = i   # now ask again for the prev step
        return goal == 0