class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        ans = nums[0]

        while l<=r:
            if nums[l] <= nums[r]:
                ans = min(ans,nums[l]) # nums[l] could be min but not 100%
            
            m = (l+r) // 2
            ans = min(ans, nums[m])

            if nums[l] <= nums[m]:  # left side is the sorted array
                ans = min(nums[l], ans) # could be min but not 100%
                l = m+1 # we got min of left side here^ now lets check right side
            else:
                ans = min(nums[l],ans)
                r = m-1
        return ans