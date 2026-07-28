class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []
 
    def _transfer(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
 
    def push(self, x):
        self.input.append(x)
 
    def pop(self):
        self._transfer()
        return self.output.pop()
 
    def peek(self):
        self._transfer()
        return self.output[-1]
 
    def empty(self):
        return not self.input and not self.output
 
 
q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())
print(q.pop())
print(q.empty())
