class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        # fill up the stack
        for i,temp in enumerate(temperatures):
            if i == 0:
                stack.append(i)
            if temp > temperatures[stack[-1]]:
                while stack and temp > temperatures[stack[-1]]:
                    result[stack[-1]] = i - stack[-1]
                    stack.pop()
            stack.append(i)
        return result