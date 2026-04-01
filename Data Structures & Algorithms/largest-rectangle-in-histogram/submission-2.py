class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # stack to store indices of heights
        res = 0
        heights.append(0)   # add a sentinel bar at the end to handle calculating the "real" last bar

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                res = max(res, height*width)
            stack.append(i)
        return res