class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ['+','-','*','/']:
                b = stack.pop()
                a = stack.pop()
                res = self.calc(a,b,t)
                stack.append(res)
            else:
                stack.append(t)
        return int(stack.pop())

    
    def calc(self,a: str,b: str, op: str) -> str:
        if op == '+':
            return str(int(a) + int(b))
        elif op == '-':
            return str(int(a) - int(b))
        elif op == '*':
            return str(int(a) * int(b))
        if op == '/':
            return str(int(int(a) / int(b)))