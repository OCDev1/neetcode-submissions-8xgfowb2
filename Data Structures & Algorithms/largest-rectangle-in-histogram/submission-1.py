class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        stack = []
        for i in range(len(heights)):
            cur_area = 0
            # add area of those before i (if possible)
            if stack:
                for j in range(0,i):
                    if stack[-1*(j+1)] >= heights[i]:
                        cur_area += heights[i]
                    else:
                        break
            
            # add the area of those after i (if possible)
            for j in range(i,len(heights)):
                if heights[j] >= heights[i]:
                    cur_area += heights[i]
                else:
                    break
            result = max(result, cur_area)
            stack.append(heights[i])
        return result

