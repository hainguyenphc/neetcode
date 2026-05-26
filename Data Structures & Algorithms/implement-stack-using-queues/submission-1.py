from collections import deque

"""
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
"""


class MyStack:
    def __init__(self):
        # Two queues alternate roles: one is active (holds data), one is a buffer.
        self._queue_1 = deque()
        self._queue_2 = deque()
        # marked=1 means queue_1 is active; marked=2 means queue_2 is active.
        self.marked = 1
        # _top caches the last pushed element to satisfy top() in O(1)
        # without using index access, which violates queue constraints.
        self._top = None

    def push(self, x: int) -> None:
        # The most recently pushed element is always the stack top.
        self._top = x
        if self.marked == 1:
            self._queue_1.append(x)
        else:
            self._queue_2.append(x)

    def pop(self) -> int:
        # Drain all but the last element from the active queue into the buffer.
        # The last remaining element is the stack top (LIFO) — pop and return it.
        # After draining, switch marked so the buffer becomes the new active queue.
        if self.marked == 1:
            if not self._queue_1:
                return
            # Single-element edge case: pop directly, no draining needed.
            if len(self._queue_1) == 1:
                popped = self._queue_1.popleft()
                self._top = None
                self.marked = 2  # switch consistently even when buffer is empty
                return popped
            while len(self._queue_1) > 1:
                popped = self._queue_1.popleft()
                self._queue_2.append(popped)
                # When only 1 element remains in queue_1, the last element moved
                # to queue_2 becomes the new top after the pop completes.
                if len(self._queue_1) == 1:
                    self._top = popped
            self.marked = 2
            return self._queue_1.popleft()
        else:
            if not self._queue_2:
                return
            # Single-element edge case: pop directly, no draining needed.
            if len(self._queue_2) == 1:
                popped = self._queue_2.popleft()
                self._top = None
                self.marked = 1  # switch consistently even when buffer is empty
                return popped
            while len(self._queue_2) > 1:
                popped = self._queue_2.popleft()
                self._queue_1.append(popped)
                if len(self._queue_2) == 1:
                    self._top = popped
            self.marked = 1
            return self._queue_2.popleft()

    def top(self) -> int:
        # Returns the cached top in O(1) using only a stored variable,
        # avoiding index access (e.g. queue[-1]) which violates queue constraints.
        return self._top
        # if self.marked == 1:
        #     return self._queue_1[-1]
        # else:
        #     return self._queue_2[-1]

    def empty(self) -> bool:
        # Stack is empty only when both queues are empty.
        return (not self._queue_1) and (not self._queue_2)


# myqueue = deque()
# myqueue.append(1)
# myqueue.append(2)
# print(myqueue[-1])
