'''
Leetcode 155. Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Keeps another stack of any encountered min values. Thus the top of min stack is always the min of number stack
pop min stack only when popping that value from number stack
All function calls are O(1) time
'''
class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins or self.mins[-1] >= val:
            self.mins.append(val)

    def pop(self) -> None:
        valu = self.stack.pop()
        if self.mins[-1] == valu:
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]