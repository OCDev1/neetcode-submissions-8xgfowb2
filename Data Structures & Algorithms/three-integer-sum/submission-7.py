class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for idx in range(len(nums)-2):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue    # Skip duplicate target nums
            i,j = idx+1, len(nums)-1 # We start 2sum on the remainder of the array (everything to the right of the current target num)

            while i<j:
                total = nums[idx]+nums[i]+nums[j]
                if total == 0:
                    ans.append([nums[idx],nums[i],nums[j]])
                    # We skip to the last occurance of duplicates
                    while i<j and nums[i]==nums[i+1]:
                        i+=1
                    while i<j and nums[j]==nums[j-1]:
                        j-=1
                    # These move us to a fresh new pair in our 2sum
                    i+=1
                    j-=1
                # Regular 2sum checks
                elif total > 0:
                    j-=1
                else:
                    i+=1
        return ans
                