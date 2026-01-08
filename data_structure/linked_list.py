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

    def reverse(self):
        prev = None
        current = self.head 
        while current and current.next:
            next_node = current.next 
            current.next = prev 
            prev = current 
            current = next_node
        self.head = prev 

    def insert_at_begining(self, value):
        current = self.head 
        new_node = Node(value)
        new_node.next = current 
        self.head = new_node

    def delete_node_by_value(self, value):

        if not self.head:
            return 

        if self.head.data ==  value:
            self.head = self.head.next 
            return 

        current = self.head
        while current.next:
            if current.next.data == value:
                current.next  = current.next.next
                return
            current = current.next 

    
    def search(self, value):
        current = self.head 
        while current:
            if current.data == value:
                return True
            current = current.next
        return False    

    def cycle_start(self):
        slow = self.head 
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break 
        else:
            return 

        slow = self.head
        while slow != fast:
            slow =slow.next
            fast = fast.next
        return slow 

    def remove_cycle(self):
        start = self.cycle_start()
        if not cycle:
            return 
        
        temp = start
        while temp.next != start:
            temp = temp.next
        temp.next = None
        
        

        
        

ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)

# create cycle manually
ll.head.next.next.next.next = ll.head.next

print(ll.floyds_cycle())  # True
print(ll.cycle_start().data)

    


        
        


