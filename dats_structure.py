# stack | last in first out

class Stack:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return self.item == []

    def push(self, value):
        self.item.append(value)
        print(self.item)


    def pop(self):
        self.item.pop()
        print(self.item)

    def peek(self):
        return self.item[-1]



s = Stack()
s.push(1)
s.pop()
print(s.is_empty())
s.push(2)
print(s.peek())

# que  | first in first out
class Que:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return self.item == []

    def push(self, value):
        self.item.append(value)

    def pop(self):
        self.item.pop()

    def peek(self):
        return self.item[0]


x =Que()
x.push(1)
x.push(2)
print(x.is_empty())
print(x.pop())
print(x.peek())


# Single Linked list

print("LINKED LIST")
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList(Node):
    def __init__(self, head):
        self.head = None

    def traverse(self):
        if self.head != None:
            current = self.head
            while current.next != None:
                print(current.item)
                current = current.next

x = LinkedList(None)
x.traverse()
