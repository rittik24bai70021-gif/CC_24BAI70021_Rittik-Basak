class MyQueue:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)
    def pop(self):
        if self.empty():
            return "Queue is Empty"

    
        if len(self.stack) == 1:
            return self.stack.pop()
        top = self.stack.pop()

        front = self.pop()
        self.stack.append(top)

        return front
    def peek(self):
        if self.empty():
            return "Queue is Empty"

        if len(self.stack) == 1:
            return self.stack[-1]

        top = self.stack.pop()
        front = self.peek()
        self.stack.append(top)

        return front
    def empty(self):
        return len(self.stack) == 0

q = MyQueue()

q.push(1)
q.push(2)
q.push(3)

print("Front Element:", q.peek())
print("Dequeued Element:", q.pop())
print("Front after Pop:", q.peek())
print("Is Queue Empty?", q.empty())