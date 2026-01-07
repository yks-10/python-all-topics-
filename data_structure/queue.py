from collections import deque
class Queue:
    def __init__(self):
        # self.items = []
        self.items = deque()

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Pop will not perform in Empty Queue")
        # return self.items.pop(0)
        return self.items.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("Pop will not perform in Empty Queue")
        return self.items[0]

    def is_empty(self):
        return not self.items

    def size(self):
        return len(self.items)

    def display(self):
        return self.items

x = Queue()
print(x.is_empty())
print(x.enqueue(1))
print(x.enqueue(1))
print(x.display())