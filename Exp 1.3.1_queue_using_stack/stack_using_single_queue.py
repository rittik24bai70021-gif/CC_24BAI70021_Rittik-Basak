from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()


    def push(self, x):
        self.q.append(x)

       
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        if self.empty():
            return "Stack is Empty"
        return self.q.popleft()

    def top(self):
        if self.empty():
            return "Stack is Empty"
        return self.q[0]
    def empty(self):
        return len(self.q) == 0
s = MyStack()

s.push(1)
s.push(2)
s.push(3)

print("Top Element:", s.top())
print("Popped Element:", s.pop())
print("Top after Pop:", s.top())
print("Is Stack Empty?", s.empty())

