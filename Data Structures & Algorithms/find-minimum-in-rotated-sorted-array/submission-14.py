class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        ans = nums[0]

        while l<=r:
            if nums[l] <= nums[r]:
                ans = min(ans,nums[l]) # nums[l] could be min but not 100%
            
            m = (l+r) // 2
            ans = min(ans, nums[m]) # could be min, last time we ever check m so lets make sure

            if nums[l] <= nums[m]:  # left side of m is the sorted array
                ans = min(nums[l], ans) # could be min but not 100%
                l = m+1 # we got min of left side here^ now lets check right side
            else:   # right side of m is sorted array
                ans = min(nums[l],ans)  # so lets grab the min here just in case
                r = m-1 # search left side
        return ans