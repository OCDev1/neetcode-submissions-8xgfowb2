class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        zero_count=0
        prod=1
        #count zeros in array
        for num in nums:
            if num==0:
                zero_count=zero_count+1

        #calculate prod w/o zeros
        for i in range(0,len(nums)):
            if nums[i] == 0:
                continue
            prod = prod*nums[i]
        
        #fill out the ans array
        for j in range(0, len(nums)):
            if zero_count > 1:
                ans.append(0)
            elif zero_count == 1:
                if nums[j] == 0:
                    ans.append(prod)
                else:
                    ans.append(0)
            else:
                ans.append(int(prod / nums[j]))
        return ans