from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)

        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
   
    def pop(self):
        if self.empty():
            return "Stack is Empty"
        return self.q1.popleft()

    def top(self):
        if self.empty():
            return "Stack is Empty"
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0

s = MyStack()

s.push(10)
s.push(20)
s.push(30)

print("Top Element:", s.top())
print("Popped Element:", s.pop())
print("Top after Pop:", s.top())
print("Is Stack Empty?", s.empty())