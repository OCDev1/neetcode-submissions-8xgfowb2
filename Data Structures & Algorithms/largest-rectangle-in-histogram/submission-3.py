class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # stack to store indices of heights
        res = 0
        heights.append(0)   # add a sentinel bar at the end to handle calculating the "real" last bar

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:    # while the current bar is shorter than the top of stack
                height = heights[stack.pop()]   # calculate area for height at the top of the stack and pop 
                if not stack:   # if the stack is empty the width is from the start
                    width = i
                else:
                    width = i - stack[-1] - 1   # if the stack isnt empty the width is from the index of the bar in the stack to the current bar
                res = max(res, height*width)
            stack.append(i)     # add current bar to stack
        return res