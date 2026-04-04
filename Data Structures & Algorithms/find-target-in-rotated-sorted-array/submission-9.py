class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1

        while l<=r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]:  # If the left half is sorted
                if nums[l] <= target <= nums[m]:    # Regular search logic
                    r = m-1
                else:
                    l = m+1
            else:   # Right half is sorted
                if nums[m] <= target <= nums[r]:    # Regular search logic
                    l = m+1
                else:
                    r = m-1
        return -1