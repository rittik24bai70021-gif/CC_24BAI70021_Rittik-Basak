class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    # Enqueue element
    def push(self, x):
        self.input.append(x)

    # Transfer elements from input stack to output stack
    def transfer(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

    # Dequeue element
    def pop(self):
        if self.empty():
            return "Queue is Empty"

        self.transfer()
        return self.output.pop()

    # Get front element
    def peek(self):
        if self.empty():
            return "Queue is Empty"

        self.transfer()
        return self.output[-1]

    # Check if queue is empty
    def empty(self):
        return len(self.input) == 0 and len(self.output) == 0


# Driver Code
q = MyQueue()

q.push(10)
q.push(20)
q.push(30)

print("Front Element:", q.peek())
print("Dequeued Element:", q.pop())
print("Front after Pop:", q.peek())
print("Is Queue Empty?", q.empty())