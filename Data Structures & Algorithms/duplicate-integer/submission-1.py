class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_map = defaultdict(int)

        for num in nums:
            if my_map[num]:
                return True
            else:
                my_map[num] = 1
        return False
         