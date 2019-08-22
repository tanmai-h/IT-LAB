class MinHeap:
	def __init__(self):
		self.heap = None
		self.size = 0
		self.index = {}

	def build_heap(self, heap):
		self.heap = heap
		self.size = len(heap)-1
		for x,y in enumerate(heap):
			self.index[y] = x
		for i in range(self.size//2, -1, -1):
			self.shift_down(i)
	
	def shift_down(self, i):
		if 2*i+1 <= self.size:
			l,r = 2*i+1,2*i+2
			m = min(self.heap[i],self.heap[l], self.heap[r])
			if m == self.heap[i]:
				return
			elif m == self.heap[l]:
				self.heap[i],self.heap[l] = self.heap[l],self.heap[i]
				self.index[self.heap[i]] = l
				self.index[self.heap[l]] = i
				self.shift_down(l)
			else:
				self.heap[i],self.heap[r] = self.heap[r],self.heap[i]
				self.index[self.heap[i]] = r
				self.index[self.heap[r]] = i
				self.shift_down(r)
		else:
			return
	def update(self, old, new):
		print(self.index[old])
		self.index[new] = self.index[old]
		print(self.index[new])
		self.heap[self.index[old]] = new
		print('val', self.heap[self.index[new]])
		self.index.pop(old)

		self.decrease_priority(self.index[new])
	def decrease_priority(self, ele):
		i = self.index[self.heap[ele]]
		self.shift_down(i)
	
	def extract_min(self):	
		m = self.heap[0]
		self.index.pop(m)
		self.heap[0] = self.heap[self.size]
		self.index[self.heap[self.size]] = 0
		self.size -= 1
		self.shift_down(0)

		return m


# class node:
# 	def __init__(self,v):
# 		self.v = v
# 	def __lt__(self, other):
# 		return self.v < other.v
# h = MinHeap()
# l = [3,2,1,15,5,4,45]

# h.build_heap(l)
# h.update(15,110)
# for i in range(7):
# 	print(h.extract_min())