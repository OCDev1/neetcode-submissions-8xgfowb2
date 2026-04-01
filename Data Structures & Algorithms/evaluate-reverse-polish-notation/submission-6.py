class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        signs = ["/","*","+","-"]
        num_stack = []

        for i in range(len(tokens)):
            # push numbers into the number stack
            if tokens[i] not in signs:
                num_stack.append(tokens[i])
            # calculate expression with current sign
            else:
                op2 = int(num_stack.pop())
                sign = tokens[i]
                op1 = int(num_stack.pop())
                if sign == '+':
                    res = int(op1 + op2)
                elif sign == '-':
                    res = int(op1 - op2)
                elif sign == '*':
                    res = int(op1 * op2)
                elif sign == '/':
                    res = int(op1 / op2)
                print(res)
                num_stack.append(res)
                res = 0
        
        return int(num_stack[0])