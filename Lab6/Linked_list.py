class Node:
    def init(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def init(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

print(ll.find_middle()) 

##
class Node:
    def init(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def init(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next          
            fast = fast.next.next     
            if slow == fast:
                return True           
        return False                 

# Test the has_cycle method
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

# Manually create a cycle for testing
ll.head.next.next.next.next.next = ll.head.next  

print(ll.has_cycle())

ll.head.next.next.next.next.next = None
print(ll.has_cycle())  

##
class Node:
    def init(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def init(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def remove_duplicates(self):
        if not self.head:
            return

        seen = set()
        current = self.head
        seen.add(current.data)  
        while current.next:
            if current.next.data in seen:
                current.next = current.next.next  
            else:
                seen.add(current.next.data)      
                current = current.next            

# Test the remove_duplicates method
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(2)
ll.append(4)
ll.append(3)

print("Before removing duplicates:")
ll.display()  

ll.remove_duplicates()

print("After removing duplicates:")
ll.display()  


##
class Node:
    def init(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def init(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    @staticmethod
    def merge_sorted(list1, list2):
        dummy = Node(0)  
        tail = dummy

        p1 = list1.head
        p2 = list2.head
        while p1 and p2:
            if p1.data < p2.data:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail = tail.next

        if p1:
            tail.next = p1
        if p2:
            tail.next = p2

        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list

ll1 = LinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(5)

ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)

print("List 1:")
ll1.display()  
print("List 2:")
ll2.display()  

merged_ll = LinkedList.merge_sorted(ll1, ll2)
print("Merged List:")
merged_ll.display()