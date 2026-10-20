class stack:
    def __init__(self) -> None:
        self.s = []
    
    def size(self):
        return len(self.s)
    
    def is_empty(self):
        return len(self.s) == 0
    
    def push(self, data):
        self.s.insert(0,data)
    
    def pop(self):
        if self.is_empty:
            print("Stack is empty")
            return
        else:
            return self.s.pop(0)
    
    def peek(self):
        if self.is_empty:
            print("Stack is empty")
            return
        else:
            return self.s[0]
        
# TODO: Make stack using append funcntion


stk = stack()
stk.push(5)
stk.push(4)
stk.push(3)
stk.push(2)
print(stk.peek())
print("---------")
print(stk.pop())
print(stk.pop())
print(stk.pop())