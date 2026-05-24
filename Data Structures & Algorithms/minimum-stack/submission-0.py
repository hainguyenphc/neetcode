class MinStack:

    def __init__(self):
        self._stack = []
        self._minStack = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        if self._minStack:
            self._minStack.append(min(val, self._minStack[-1]))
        else:
            self._minStack.append(val)

    def pop(self) -> None:
        self._stack.pop()
        self._minStack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._minStack[-1]


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(1)
    minStack.push(2)
    minStack.push(0)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())
