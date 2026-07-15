class MinStack:

    def __init__(self):
        self.stack = []
        self.minium_value_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minium_value_stack[-1] if  self.minium_value_stack else val)
        self.minium_value_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minium_value_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minium_value_stack[-1]
