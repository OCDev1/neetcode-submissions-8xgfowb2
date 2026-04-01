class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        all_trips=[]

        nums.sort()
        
        low=0
        high=len(nums)-1

        for i in range(len(nums)):
            low=i+1
            high=len(nums)-1

            if i > 0 and nums[i]==nums[i-1]:
                continue

            while low < high:     
                sum = nums[low]+nums[high] + nums[i]
                if sum > 0:
                    high -= 1
                elif sum < 0:
                    low+=1
                
                else:
                    all_trips.append([nums[low] ,nums[high], nums[i]])
                    low+=1
                    while (low < high and nums[low] == nums[low-1]):
                        low += 1  #this is enough because high pointer will have to be moved to smaller value
            
        return all_trips
