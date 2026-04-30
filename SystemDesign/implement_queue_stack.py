
class MyQueue:
    def __init__(self):
        # Create an attribute that holds the empty queue of inner and outter
        self.inner = []
        self.outer = []



    def push(self, x: int) -> None:
        self._move()
        return self.inner.append(x)
        

    def pop(self) -> int:
        # Removes the element from the front of the queue and returns it.
        self._move()
        return self.outer.pop()

    def peek(self) -> int:
        # Description  Returns the element at the front of the queue.
        # So wwanna put the element into the front of the inner queue
        self._move()
        return self.outer[-1]
        

    def empty(self) -> bool:
        # Description Returns true if the queue is empty, false otherwise.
        return not self.inner and not self.outer

    # A helper method that'll allow me to move remove element itself from the outer queue
    def _move(self):
        if not self.outer:
            while self.inner:
                self.outer.append(self.inner.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()