class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)
    def transfer(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

    def pop(self):
        if self.empty():
            return "Queue is Empty"

        self.transfer()
        return self.output.pop()

    def peek(self):
        if self.empty():
            return "Queue is Empty"

        self.transfer()
        return self.output[-1]

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
