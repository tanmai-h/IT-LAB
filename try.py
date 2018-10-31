from collections import deque
class Stack:
	def __init__(self):
		self.T=deque()
	def push(self,x):
		self.T.addFirst(x)
	def pop(self):
		self.T.removeFirst()
	def top(self):
		return self.T.peekFront()	



s=Stack()
s.push(4)
s.push(10)
print(s.top())
s.pop()
print(s.top())
