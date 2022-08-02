

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	def __repr__(self):
		return f"Node with data({type(self.data)}): {self.data}"

	def get_next(self):
		return self.next

	def set_next(self, new_node):
		self.next = new_node

	def get_data(self):
		return self.data

class LinkedList:
	def __init__(self):
		self.length = 0
		self.head = None

	def __len__(self):
		return self.length

	def __repr__(self):
		return f"SinglyLinkedList with {self.length} items"

	def get_nodes(self):
		if self.length < 1:
			print("No nodes in SinglyLinkedList.")
		else:
			current_node = self.head
			# iterate through all nodes after head
			while current_node:
				print(current_node)
				current_node = current_node.get_next()

	def get_head(self):
		return self.head

	def set_head(self, new_head):
		self.head = new_head

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
			while last_node.get_next():
				last_node = last_node.get_next()
			# set new Node as next for the last node
			last_node.set_next(new_node)
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
			node.set_next(self.head)
			# set head to new node
			self.node(node)
			# iterate length by 1
			self.length += 1
		else:
			# iterate through LinkedList until the node before the given index
			node_before = self.head
			for x in range(0, index - 1):
				node_before = node_before.get_next()
			# set new node's next pointer to node_before's next pointer
			node.set_next(node_before.get_next())
			# set node_before's next pointer to new node
			node_before.set_next(node)
			# iterate length by 1
			self.length += 1


	def remove(self):
		# if there is at least one node in the Linked List
		if self.length > 0:
			# set new head as the next closest node in the Linked List
			self.head = self.head.get_next()
			# decrement length by 1
			self.length -= 1
		else:
			print("SinglyLinkedList is empty, nothing to remove.")

	def remove(self, node):
		# check if LinkedList is empty
		if self.length > 0:
			current_node = self.head
			# iterate through all items to see if 
			while current_node:
				# if the current node matches the arg node, then we need to remove the node from the LinkedList
				if current_node.get_data() == node.get_data():
					# if the node to be removed is the head
					if current_node is self.head:
						self.head = self.head.get_next()
					# if the node is anywhere else in the list
					else:
						pass
		
		# if length is 1, then do a single comparison with node
		elif self.length == 1:
			if self.head.get_data == node.get_data():
				self.head = None
				self.length -= 1
		# if length is 0, then there is nothing to remove
		else:
			print("SinglyLinkedList is empty, nothing to remove.")
