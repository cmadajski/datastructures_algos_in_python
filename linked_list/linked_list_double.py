

class Node:
    def __init__(self, data=None, prev=None, next=None):
        # doubly linked list node requires data, prev, next
        self.data = data
        self.prev = prev
        self.next = next

    def __len__(self):
        return len(self.data)

    def __str__(self):
    	# get string representation of the data's data type
    	base_data_type = str(type(self.data))
		# format data type (data type name always starts at index 8)
	    end_index = base_data_type.index("'", 8)
	    formatted_data_type = base_data_type[8:end_index]
	    return f"Node with {formatted_data_type} data: {self.data}"

    def __repr__(self):
	    # get string representation of the data's data type
	    base_data_type = str(type(self.data))
	    # format data type (data type name always starts at index 8)
	    end_index = base_data_type.index("'", 8)
	    formatted_data_type = base_data_type[8:end_index]
	    return f"Node with {formatted_data_type} data: {self.data}"

class DoublyLinkedList:
    def __init__(self):
        # for doubly linked list we need length, head, tail
        self.length = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.length

    def __repr__(self):
        string = "\n"
        
        return f"DoublyLinkedList with {self.length} items."

    def __str__(self):
        return 

    
