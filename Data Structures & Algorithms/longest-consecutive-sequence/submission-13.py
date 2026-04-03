class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        allNums = set(nums)
        ans = 0

        for num in nums:
            length = 1
            if num - 1 in allNums:
                continue    # Skip nums that are middle of sequence
            while num + length in allNums:
                length += 1
            ans = max(length, ans)  # Save longest sequence
        return ans