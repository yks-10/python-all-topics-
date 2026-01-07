class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)


    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()
        

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        return not self.items

    def size(self):
        return len(self.items)

x = Stack()
print(x.is_empty())