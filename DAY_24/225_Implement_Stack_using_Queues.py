class MyStack(object):

    def __init__(self):
        self.stack=[]

    def push(self, x):
        self.stack.append(x)
        

    def pop(self):
        if self.stack is None:
            return  
        return self.stack.pop()
        

    def top(self):
        if self.stack is None:
            return
        return self.stack[-1]
        

    def empty(self):
        if not self.stack:
            return True
        else:
            return False
        