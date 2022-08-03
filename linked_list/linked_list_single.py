from multipledispatch import dispatch

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

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

	def __del__(self):
		print(f"Node with data {self.data} has been destroyed.")

class LinkedList:
	def __init__(self):
		self.length = 0
		self.head = None

	def __len__(self):
		return self.length

	def __repr__(self):
		if self.length < 1:
			return "No nodes in SinglyLinkedList."
		else:
			string = "\n"
			current_node = self.head
			# iterate through all nodes after head
			while current_node:
				string += repr(current_node) + "\n"
				current_node = current_node.next
			return string

	def __str__(self):
		if self.length < 1:
			return "No nodes in SinglyLinkedList."
		else:
			string = "\n"
			current_node = self.head
			# iterate through all nodes after head
			while current_node:
				string += repr(current_node) + "\n"
				current_node = current_node.next
			return string

	@dispatch(Node)
	def append(self, new_node):
		"""Append a new Node to the end of the existing Linked List"""
		# if the LinkedList is empty
		if self.length == 0:
			# insert new Node as head
			self.head = new_node
			# increment length by 1
			self.length += 1
		# if the LinkedList has 1 or more items
		else:
			# traverse to the end of the LinkedList
			# start at current head
			last_node = self.head
			# loop will continue until it finds a node with None as the next node
			while last_node.next:
				last_node = last_node.next
			# set new Node as next for the last node
			last_node.next = new_node
			# increment length by 1
			self.length += 1

	@dispatch(int)
	def append(self, num: int):
		"""Append a new Node to the end of the existing Linked List."""
		# if LinkedList is empty
		if self.length == 0:
			# insert new Node as head
			self.head = Node(num)
			# increment length by 1
			self.length += 1
		# if the LinkedList has 1 or more items
		else:
			# traverse to the end of the LinkedList
			# start at current head
			last_node = self.head
			# loop will continue until it finds a node with None as the next node
			while last_node.next:
				last_node = last_node.next
			# set new Node as next for the last node
			last_node.next = Node(num)
			# increment length by 1
			self.length += 1

	def insert(self, node, index=-1):
		"""Inserts a node at a specified index (defaults to end of list)"""
		# if index does not exist, prompt user
		if index > self.length - 1 or index < -1:
			print(f"Can't insert {node} at position {index}, index is out of bounds.")
		# if index is default, call append to add node to the end of the list
		elif index == -1:
			append(node)
		# if index is the same as head
		elif index == 0:
			# set node's next pointer to current head
			node.next = self.head
			# set head to new node
			self.node(node)
			# iterate length by 1
			self.length += 1
		else:
			# iterate through LinkedList until the node before the given index
			node_before = self.head
			for x in range(0, index - 1):
				node_before = node_before.next
			# set new node's next pointer to node_before's next pointer
			node.next = node_before.next
			# set node_before's next pointer to new node
			node_before.next = node
			# iterate length by 1
			self.length += 1


	def remove_head(self):
		# if there is at least one node in the Linked List
		if self.length > 0:
			# get the item next to head
			self.head = self.head.next
			# decrement length by 1
			self.length -= 1
		else:
			print("SinglyLinkedList is empty, nothing to remove.")

	@dispatch()
	def remove(self):
		"""Removes the last item from the LinkedList"""
		if self.length < 1:
			print("SinglyLinkedList is empty, nothing to remove.")
		elif self.length == 1:
			# set new head as the next closest node in the Linked List
			self.head = self.head.next
			# decrement length by 1
			self.length -= 1
		else:
			node_before = self.head
			# traverse all nodes until you reach a node with a next pointer of None (the last node)
			while node_before.next.next:
				node_before = node_before.next
			# set node_before's next pointer to null to disassociate last node from the LinkedList
			node_before.next = None
			# decrement length by 1
			self.length -= 1

	@dispatch(Node)
	def remove(self, node):
		# if LinkedList is NOT empty
		if self.length > 0:
			current_node = self.head
			# check to see if head matches the arg node
			if current_node == node.data:
				self.head = self.head.next
				self.length -= 1
			else:
				while current_node.next:
					# if the next node matches the arg node, then we need to remove that node from the LinkedList
					if current_node.next.data == node.data:
						# set current node's pointer to next node's next pointer
						current_node.next = current_node.next.next
						# decrement length by 1
						self.length -= 1
		
		# if length is 0, then there is nothing to remove
		else:
			print("SinglyLinkedList is empty, nothing to remove.")

	@dispatch(int)
	def remove(self, index):
		if index > self.length - 1 or index < 0:
			print(f"Could not remove Node at index {index}, index is out of bounds.")
		else:
			# if the index is the same as head
			if index == 0:
				self.head = self.head.next
				self.length -= 1
			else:
				node_before = self.head
				# iterate through nodes until node before index
				iterator = 0
				while iterator < index - 1:
					node_before = node_before.next
					iterator += 1
				# set node_before's next pointer to the node after the removed node
				node_before.next = node_before.next.next
				# decrement length by 1
				self.length -= 1