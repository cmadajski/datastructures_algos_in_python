# define a node class for singly linked list
class Node():
    # create constructor for node instantiation
    def __init__(self, value, next_node=None):
        # holds a value for a node
        self.value = value
        # keeps track of the next node in the sequence
        self.next_node = next_node

    # getter for node value
    def get_value(self):
        return self.value
    
    # getter for node next pointer
    def get_next_node(self):
        return self.next_node

    # setter for node next pointer
    def set_next_node(self, new_node):
        self.next_node = new_node
    
    # no getter for node value, nodes are immutable except for positioning in the list


def test_node():
    

def test_linkedlist():
    pass

if __name__ == '__main__':
    print("Testing Node and Linked List implementations:")
    test_node()
    test_linkedlist()