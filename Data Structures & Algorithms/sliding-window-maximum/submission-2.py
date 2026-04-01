class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        
        cur_max = -1001
        max_index = -1
        start = 0
        end = k
        while end <= len(nums):
            # find max in current window
            for i in range(start,end):
                cur_max = max (cur_max, nums[i])
            ans.append(cur_max)
            cur_max=-1001
            start+=1
            end+=1
        return ans

        