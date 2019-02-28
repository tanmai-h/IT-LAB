class MinHeap:
    def __init__(self, func):
        self.heap = [0]
        self.size = 0
        self.func = func
    def shiftUp(self,i):
        if(i // 2 > 0):
            if self.func(self.heap[i]) < self.func(self.heap[i // 2]):
                self.swap(i, i // 2)
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

    def buildHeap(self,ll):
        self.size = len(ll)
        self.heap = [0] + ll[:]
        for i in range(len(ll) // 2, 0, -1):
            self.shiftDown(i)