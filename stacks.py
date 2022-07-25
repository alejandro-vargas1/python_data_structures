class Stack:
    def __init__(self):
        self.top = 0
        self.stack = []
    
    def stack_empty(self):
        if self.top == 0:
            return True
        else:
            return False
    
    def push(self, value):
        self.top += 1
        self.stack.append(value)
    
    def pop(self):
        import pdb; pdb.set_trace()
        if self.stack_empty():
            raise ValueError("It's empty")
        else:
            self.top -= 1
            return self.stack.pop()

if __name__ == '__main__':
    stack = Stack()
    import pdb; pdb.set_trace()