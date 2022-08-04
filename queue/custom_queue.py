class CustomQueue:
    def __init__(self, max_length: int = 5):
        self.max_length = max_length
        self.length = 0
        self.data = list()
    
    def __repr__(self):
        return f"CustomQueue of length {self.length} with data: {self.data}\nMax length {self.max_length} items ({self.max_length - self.length} items remaining)."

    def __str__(self):
        return f"CustomQueue of length {self.length} with data: {self.data}\nMax length {self.max_length} items ({self.max_length - self.length} items remaining)."

    def __del__(self):
        return f"CustomQueue of length {self.length} with data {self.data} has been deleted."

    @dispatch(int)
    def push(self, value) -> None:
        if len(self.data) >= self.max_length:
            print("OVERFLOW ERROR: Queue has reached maximum capacity.")
        else:
            self.data.append(value)
            self.length += 1

    def pop(self, index: int = 0):
        """Pop returns the item at the front of the queue, unless the queue is empty (resulting in an underflow error)."""
        if self.length < 1:
            print("UNDERFLOW ERROR: Queue is empty.")
        else:
            self.length -= 1
            return self.data.pop(0)
            