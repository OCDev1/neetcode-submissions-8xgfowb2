class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False
        
        target = sum(nums)//2

        a = [[False] * (target+1) for _ in range(len(nums)+1)]
        
        for i in range(len(nums)):
            a[i][0] = True

        for x in range(1, len(nums)):
            for y in range(1, target+1):
                a[x][y] = a[x-1][y-nums[x]] or a[x-1][y]
        
        return a[len(nums)-1][target]

        
        

        


