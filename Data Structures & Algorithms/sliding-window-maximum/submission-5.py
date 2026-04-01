class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []

        for i in range(len(nums)):
            # remove indices out of range
            if dq and dq[0] < i-k+1:
                dq.popleft()
            
            # remove all values smaller than the new value
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            # append from right to the dequeue
            dq.append(i)

            # start adding the maxes to the list only after the first window reached size k
            if i >= k-1:
                result.append(nums[dq[0]])
        return result