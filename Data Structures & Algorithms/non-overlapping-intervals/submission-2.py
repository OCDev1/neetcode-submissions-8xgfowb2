class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        prev_end = intervals[0][1]

        ans = 0

        for interval in intervals:
            if interval[0] < prev_end:
                ans += 1
            else:
                prev_end = interval[1]
        
        return ans-1