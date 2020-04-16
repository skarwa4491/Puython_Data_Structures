class Stack():
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()

    def isempty(self):
        return self.items==[]

    def peek(self):
        if(self.isempty()):
            return self.items[-1]
        else:
            return "Stack is empty"

    def get_stack(self):
        return self.items
