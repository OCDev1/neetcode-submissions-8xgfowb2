class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def calc(self, L, R):
            return (min(heights[L], heights[R]) * (R-L))
        
        max_water = 0
        l = 0
        r = len(heights)-1
        while l < r:
            max_water = max(max_water, calc(self, l, r))
            if heights[l] > heights[r]:
                r-=1
            elif heights[l] <= heights[r]:
                l += 1
        return max_water