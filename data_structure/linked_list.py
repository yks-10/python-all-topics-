class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 

        
    def push(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return 

        temp = self.head 
        while temp.next:
            temp = temp.next 
        
        temp.next = new_node 

    def traversal(self):
        temp = self.head
        while temp:
            print(temp.data, end="")
            temp = temp.next
        print("None")

    
    def floyds_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            if slow == fast:
                return True
        return False

    


        
        


