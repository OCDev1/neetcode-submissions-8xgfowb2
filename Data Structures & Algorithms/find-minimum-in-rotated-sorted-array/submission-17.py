class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        ans = 1001  # max value + 1
        while l<=r:
            m = (l+r) // 2

            if nums[l] <= nums[m]:
                ans = min(ans, nums[l])
                l = m+1
            else:
                ans = min(ans, nums[m])
                r = m-1
        return ans