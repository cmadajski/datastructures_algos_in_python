# define a Node class
class Node():
    # create constructor for Node instantiation
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_node):
        self.next_node = new_node


def test_node():
    pass

def test_linkedlist():
    pass

if __name__ == '__main__':
    print("Testing Node and Linked List implementations:")
    test_node()
    test_linkedlist()