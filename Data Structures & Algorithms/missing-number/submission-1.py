class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        myset = set()
        for i in range(len(nums)):
            myset.add(nums[i])
        
        for i in range(len(nums)+1):
            if i not in myset:
                return i
            