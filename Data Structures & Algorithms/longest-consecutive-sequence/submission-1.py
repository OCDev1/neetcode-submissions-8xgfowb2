class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        longest=0

        for num in numset:
            length = 0
            while(num+length in numset):
                length+=1
                longest = max(longest, length)
    
        return longest


