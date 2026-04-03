class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = 1

        allNums = set(nums) # Quickly find all nums

        for num in allNums: # Avoid duplicates
            if num - 1 in allNums:  # If the number is a middle of sequence
                continue    # Skip it
            length = 1
            while num + length in allNums:
                length += 1
            ans = max(ans,length)
        return ans