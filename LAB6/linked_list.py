class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


class LinkedList:
    # ... (previous code)

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

# Test the append method
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)


class LinkedList:
    # ... (previous code)

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

# Test the display method
ll.display()  # Output: 1 -> 2 -> 3



class LinkedList:
    # ... (previous code)

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

# Test the insert method
ll.insert(4, 1)
ll.display()  # Output: 1 -> 4 -> 2 -> 3


class LinkedList:
    # ... (previous code)

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

# Test the delete method
ll.delete(2)
ll.display()  # Output: 1 -> 4 -> 3



class LinkedList:
    # ... (previous code)

    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

# Test the search method
print(ll.search(4))  # Output: 1
print(ll.search(5))  # Output: -1



class LinkedList:
    # ... (previous code)

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Test the reverse method
ll.reverse()
ll.display()  # Output: 3 -> 4 -> 1



# Exercise 
#1. Finding the middle element of the linked list

class LinkedList:
   

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

# Example usage:
ll = LinkedList()
for i in range(1, 6):
    ll.append(i)  # Linked list: 1 -> 2 -> 3 -> 4 -> 5
print("Middle element:", ll.find_middle())  

#2. Detecting if the linked list has a cycle

class LinkedList:

    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# Example usage:
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.head.next.next.next = ll.head  # Creating a cycle
print("Has cycle:", ll.has_cycle()) 

#3. Removing duplicates from an unsorted linked list

class LinkedList:
   

    def remove_duplicates(self):
        current = self.head
        prev = None
        seen = set()
        while current:
            if current.data in seen:
                prev.next = current.next
            else:
                seen.add(current.data)
                prev = current
            current = current.next

# Example usage:
ll = LinkedList()
for i in [1, 2, 3, 2, 1]:
    ll.append(i)
ll.remove_duplicates()
ll.display() 

#4. Merging two sorted linked lists into a single sorted linked list

class LinkedList:
 

    @staticmethod
    def merge_sorted(list1, list2):
        dummy = Node(0)
        tail = dummy
        current1 = list1.head
        current2 = list2.head

        while current1 and current2:
            if current1.data < current2.data:
                tail.next = current1
                current1 = current1.next
            else:
                tail.next = current2
                current2 = current2.next
            tail = tail.next

        tail.next = current1 if current1 else current2
        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list

# Example usage:
ll1 = LinkedList()
ll2 = LinkedList()
for i in [1,6]