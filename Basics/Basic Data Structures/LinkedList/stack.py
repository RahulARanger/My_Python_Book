from linked_list import DoubleNode, SingleNode
import typing

class SimpleStack:
	def __init__(self):
		self.head: typing.Optional[SingleNode] =  None
		self.length = 0

	def append(self, node):
		node = SingleNode(node)
		self.length += 1

		if not self.head:
			self.head = node
			return 

		self.head.pre_append(node)

	def pop(self):
		store = self.head
		
		if self.head:
			self.head = self.head.next
			self.length -= 1
		
		return store

	def top(self):
		return self.head.value if self.head else None

	def isEmpty(self):
		return self.head is None

	def __str__(self):
		return str(self.head)

