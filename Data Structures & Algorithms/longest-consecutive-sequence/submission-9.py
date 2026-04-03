class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = 1

        seen = set()
        allNums = set()
        for num in nums:
            allNums.add(num)

        for i in range(len(nums)):
            max_len = 1
            seen.add(nums[i])
            if nums[i]-1 in seen:
                continue   # This is not a sequence start point - its a middle
            
            # Start sequence length check
            for j in range(1,len(nums)):
                if nums[i]+j in allNums:
                    seen.add(nums[i]+j)
                    max_len+=1
                else:
                    break
            ans = max(max_len,ans)
        return ans