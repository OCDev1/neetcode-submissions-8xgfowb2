class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Find max product for all l, r combos where l <= r
        arr = [[1] * len(nums) for _ in range(len(nums))]

        # base cases
        for r in range(len(nums)):
            arr[0][0] = nums[0]
        # populate dp array
        for l in range(0,len(nums)):
            for r in range(1,len(nums)):
                if l > r:
                    arr[l][r] = 0
                if l == r:
                    arr[l][r] = nums[l]
                else:
                    arr[l][r] = arr[l][r-1] * nums[r]

        ans = float('-inf')
        for l in range(len(nums)):
            for r in range(len(nums)):
                if l > r:
                    continue
                else:
                    ans = max(ans, arr[l][r])
        return int(ans)