class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        for num in nums:
            if num == 0:
                zeroCount += 1
        if zeroCount > 1:
            return [0] * len(nums)

        productOfAll = 1
        for num in nums:
            if num != 0:
                productOfAll *= num

        ans = []
        for num in nums:
            if num == 0:
               ans.append(productOfAll)
            elif 0 in nums:
                ans.append(0)
            else:
                ans.append(int(productOfAll / num))
        
        return ans