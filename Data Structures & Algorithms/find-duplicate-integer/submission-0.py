class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        my_set = set()

        for num in nums:
            if num not in my_set:
                my_set.add(num)
            else:
                return num