class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # At each step we will ask ourselves:
        # is nums[i] better of alone? or better with the current window product?

        res = nums[0]
        cur_window_max = 1
        cur_window_min = 1  # for mult we track minimum because it could become maximum

        for num in nums:
            temp_max = num * cur_window_max
            temp_min = num * cur_window_min
            # max between restarting window or extending window
            cur_window_max = max(num, temp_max, temp_min)
            # track min as well
            cur_window_min = min(num, temp_max, temp_min)
            # track global max
            res = max(res, cur_window_max)
        return res