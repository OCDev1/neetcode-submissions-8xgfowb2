class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # We ask - am I in the sorted or unsorted part of the array?
        # If sorted - is target in this part? if not - recurse on the other half
        l,r = 0, len(nums)-1

        while l<=r:
            m = (l+r) // 2

            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]:   # left half is sorted
                if nums[l] <= target < nums[m]:   # is target in this half?
                    r = m # yes - search this half
                else:
                    l = m+1 # no - search again in other half
            else:   # right half is sorted
                if nums[m] < target <= nums[r]:   # is target in sorted half?
                    l = m # yes - search this half
                else:
                    r = m-1 # no - search again in other half
        return -1