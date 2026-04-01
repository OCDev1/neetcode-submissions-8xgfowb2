class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def calc(self, L, R):
            return (min(heights[L], heights[R]) * (R-L))
        
        max_water = 0
        l = 0
        for l in range(len(heights)):
            r = len(heights)-1
            while l < r:
                max_water = max(max_water, calc(self, l, r))
                r-=1
        return max_water