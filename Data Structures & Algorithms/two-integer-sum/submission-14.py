class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = defaultdict(int)

        # populating hash map
        for i in range(len(nums)):
            my_map[nums[i]] = i
        
        for i in range(len(nums)):
            if my_map[target-nums[i]] and (i != my_map[target-nums[i]]):
                return [i,my_map[target-nums[i]]]