class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ['+','-','*','/']:
                b,a = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(int(a) + int(b))
                elif t == '-':
                    stack.append(int(a) - int(b))
                elif t == '*':
                    stack.append(int(a) * int(b))
                elif t == '/':
                    stack.append(int(int(a) / int(b)))
            else:
                stack.append(t)
        return int(stack.pop())