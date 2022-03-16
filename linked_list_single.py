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

class LinkedList():
    def __init__(self, node: Node):
        self.head = node
        self.num_nodes = 0
        curr_node = self.head
        while curr_node:
            self.num_nodes += 1
            curr_node = curr_node.get_next_node()

def test_node():
    # testing values
    num_errors = 0

    # tests
    node1 = Node(34)
    valueTest1 = node1.get_value()
    if valueTest1 != 34:
        num_errors += 1
        print("Test 1 fail")

    node2 = Node("This is text", node1)
    valueTest2 = node2.get_value()
    valueTest3 = node2.get_next_node()
    if valueTest2 != "This is text":
        num_errors += 1
        print("Test 2 fail")
    if valueTest3.get_value() != 34:
        num_errors += 1
        print("Test 3 fail")

    print(f'There are {num_errors} errors in the Node class.')
    if num_errors > 0:
        print("You've got debugging to do.")
    else:
        print("Your code is bug free.")


def test_linkedlist():
    pass

if __name__ == '__main__':
    print("Testing Node implementation:")
    test_node()
    # test_linkedlist()