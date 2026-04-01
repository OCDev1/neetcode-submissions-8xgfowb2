class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while l <= r:
            if (r-l+1) < 3:
                return min(nums[l:r+1])
            
            m = (r + l) // 2

            if nums[m] < nums[m+1] and nums[m] < nums[m-1]:
                return nums[m]
            
            elif nums[m-1] < nums[r]:
                r = m - 1
            elif nums[m-1] > nums[r]:
                l = m + 1