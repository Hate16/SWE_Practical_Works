class Node:
    def _init(self, data):  # Corrected to __init_
        self.data = data
        self.next = None

class LinkedList:
    def _init(self):  # Corrected to __init_
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

    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next          
            fast = fast.next.next     
            if slow == fast:
                return True           
        return False

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

# Testing the LinkedList methods
# Test find_middle
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

print("Middle element:", ll.find_middle())

# Test has_cycle
ll_with_cycle = LinkedList()
ll_with_cycle.append(1)
ll_with_cycle.append(2)
ll_with_cycle.append(3)
ll_with_cycle.append(4)
ll_with_cycle.append(5)

# Manually create a cycle for testing
ll_with_cycle.head.next.next.next.next.next = ll_with_cycle.head.next  
print("Has cycle:", ll_with_cycle.has_cycle())  # Should print True

# Break the cycle
ll_with_cycle.head.next.next.next.next.next = None
print("Has cycle after breaking:", ll_with_cycle.has_cycle())  # Should print False

# Test remove_duplicates
ll_duplicates = LinkedList()
ll_duplicates.append(1)
ll_duplicates.append(2)
ll_duplicates.append(3)
ll_duplicates.append(2)
ll_duplicates.append(4)
ll_duplicates.append(3)

print("Before removing duplicates:")
ll_duplicates.display()  

ll_duplicates.remove_duplicates()

print("After removing duplicates:")
ll_duplicates.display()  

# Test merge_sorted
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
