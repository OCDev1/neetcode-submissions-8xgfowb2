class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # This is similar to 2sum, except our "target" is nums[i]
        # and our 2 pointers are j,k
        # We need to sort the array first
        # index i will go from 0 to len(nums)-3 and inside the loop we run the
        # 2 sum algorithm with (-1 * nums[i]) as the target number
        nums.sort()
        seen = set()
        ans = []
        for i in range(len(nums)-2):
            # run the 2 sum algo with target = -1 * nums[i]
            # why? nums[i] + nums[j] + nums[k] == 0 -> nums[j]+nums[k] == -1*nums[i]
            target = -1*nums[i]
            j,k = i+1, len(nums)-1
            while j < k:
                if nums[j]+nums[k] == target:
                    seen.add((nums[i],nums[j],nums[k]))
                    j += 1  #move pointer so loop can continue
                elif nums[j]+nums[k] > target:
                    k -= 1
                else:
                    j += 1
        for triplet in seen:
            ans.append(list(triplet))
        return ans