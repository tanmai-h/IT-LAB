class MinHeap:
    def __init__(self, func=None):
        self.heap = [0]
        self.size = 0
        if func is None:
            self.func = lambda x:x
        else:
            self.func = func
        self.indices = {}
    def shiftUp(self,i):
        if(i // 2 > 0):
            if self.func(self.heap[i]) < self.func(self.heap[i // 2]):
                self.swap(i, i // 2)
                t = self.indices[i // 2]
                self.indices[i // 2] = i
                self.indices[i] = t
                self.shiftUp(i // 2)
    def insert(self,k):
        self.heap.append(k)
        self.size = self.size + 1
        self.shiftUp(self.size)

    def shiftDown(self,i):
        if(2*i <= self.size):
            max = self.maxChild(i)
            if (max != i) and self.func(self.heap[i]) > self.func(self.heap[max]):
                self.swap(i, max)
                #t = self.indices[max]
                #self.indices[max] = i
                #self.indices[i] = t
                self.shiftDown(max)
            else:
                return
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j] ,self.heap[i]
    
    def maxChild(self,i):
        l = 2*i
        r = l+1
        if l > self.size:
            return i
        elif r > self.size:
            return l
        else:
            max = l if self.heap[l] > self.heap[r] else r
            return max
    def extractMin(self):
        retval = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size = self.size - 1
        self.heap.pop()
        self.shiftDown(1)
        
        return retval
    def updatePriority(self, i, dir='up'):
        if dir == 'up':
            self.shiftUp(self.indices[i])
        else:
            self.shiftDown(self.indices[i])
    def buildHeap(self,ll):
        self.size = len(ll)
        for x,y in enumerate(ll):
            self.indices[y] = x
        self.heap = [0] + ll[:]
        for i in range(len(ll) // 2, 0, -1):
            self.shiftDown(i)
# class MinHeap:
#     def __init__(self, func=None):
#         self.heap = []
#         self.size = 0
#         if func is None:
#             self.func = lambda x:x
#         else:
#             self.func = func
#         self.indices = {}
    
#     def shiftUp(self, index):
#         while (index //2 > 0):
#             if self.func(self.heap[index]) < self.func(self.heap[index//2]):
#                 self.indices[self.heap[index]] = index // 2
#                 self.indices[self.heap[index//2]] = index
#                 self.heap[index],self.heap[index//2] = self.heap[index//2],self.heap[index]
#                 index = index // 2
#             else:
#                 break

#     def insert(self, i):
#         self.heap.append(i)
#         self.indices[i] = size+1
#         self.size += 1
#         self.shiftUp(self.size)

#     def extractMin(self):
#         ret = self.heap[0]
    
