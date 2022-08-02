

class Node:
    def __init__(self, data=None, prev=None, next=None):
        # doubly linked list node requires data, prev, next
        self.data = data
        self.prev = prev
        self.next = next

    def __len__(self):
        return len(self.data)

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_next(self, new_next):
        self.next = new_next

    def set_prev(self, new_prev):
        self.prev = new_prev

class DoublyLinkedList:
    def __init__(self):
        # for doubly linked list we need length, head, tail
        self.length = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.length

    def __repr__(self):
        return f"DoublyLinkedList with {self.length} items."

    
