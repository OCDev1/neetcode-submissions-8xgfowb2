class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        ans = [intervals[0]]

        for start, end in intervals:
            prev_end = ans[-1][1]

            if start <= prev_end:
                ans[-1][1] = max(prev_end, end) # change end of interval in ans to longest of the two 
            else:
                ans.append([start, end])
        return ans