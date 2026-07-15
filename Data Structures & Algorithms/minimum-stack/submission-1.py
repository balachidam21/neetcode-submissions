class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum_value_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minimum_value_stack[-1] if  self.minimum_value_stack else val)
        self.minimum_value_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minimum_value_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum_value_stack[-1]
