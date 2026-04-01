class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        middle = len(nums)//2
        print(nums)
        if target == nums[middle]:
            return middle
        if len(nums) == 1:
            return -1
        elif target > nums[middle]:
            result = self.search(nums[middle+1:],target)
            if result == -1:
                return -1
            else:
                return middle+1+result
        else:
            return self.search(nums[:middle],target)