MAX = 100

class Stack:
	"""Define the Stack class here.
	   Write a constructor and implement the push, pop and isEmpty functions
	   using Python lists.
	"""
	def __init__(self):
		self.l = [None for i in range(MAX)]
		self.top = -1
	def isEmpty(self):
		if self.top == -1:
			return True
		return False
	def isFull(self):
		if self.top >= MAX-1:
			return True
		return  False
	def topE(self):
		return self.l[self.top]
	def pop(self):
		if self.isEmpty() is True:
			print("cant pop from empty stack")
			return
		e = self.topE()
		self.top += -1
		return e
	def push(self, x):
		if self.isFull() is True:
			print("cant push into full stack")
			return
		self.top += 1
		self.l[self.top] = x
	def __str__(self):
		st = ""
		i = self.top
		while i >= 0:
			st += str(self.l[i]) + "\n"
			i -= 1
		return st