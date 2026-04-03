class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = 1

        seen = set()
        for num in nums:
            seen.add(num)

        for i in range(len(nums)):
            max_len = 1
            for j in range(1,len(nums)):
                if nums[i]+j in seen:
                    max_len+=1
                else:
                    break
            ans = max(max_len,ans)
        return ans