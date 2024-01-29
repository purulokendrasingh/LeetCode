class MyQueue:

    def __init__(self):
        self.s = Stack()
        self.temp = Stack()

    def push(self, x: int) -> None:
        while not self.s.is_empty():
            self.temp.push(self.s.pop())
            
        self.s.push(x)
        while not self.temp.is_empty():
            self.s.push(self.temp.pop())
        

    def pop(self) -> int:
        return self.s.pop()

    def peek(self) -> int:
        if self.s.is_empty():
            return None
        return self.s.peek()

    def empty(self) -> bool:
        return self.s.is_empty()
        
class Stack:
    
    def __init__(self):
        self.s = deque()
        
    def push(self, x: int) -> None:
        self.s.appendleft(x)
        
    def pop(self) -> int:
        return self.s.popleft()
    
    def peek(self) -> int:
        return self.s[0]
    
    def length(self) -> int:
        return len(self.s)
    
    def is_empty(self) -> bool:
        return self.length() == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()