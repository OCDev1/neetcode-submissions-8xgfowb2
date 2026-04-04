class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []  # Monotonic stack

    def push(self, val: int) -> None:
        self.stack.append(val)  # Append to regular stack
        if not self.minStack or self.minStack[-1] >= val:  # Append to minStack only if val is new Min or stack is empty
            self.minStack.append(val)

    def pop(self) -> None:
        tmp = self.stack.pop()
        if self.minStack[-1] == tmp:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]