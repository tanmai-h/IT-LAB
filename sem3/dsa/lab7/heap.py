class BinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def shiftUp(self,i):
        if(i // 2 > 0):
            if self.heap[i] > self.heap[i // 2]:
                self.swap(i, i // 2)
                self.shiftUp(i // 2)
    def insert(self,k):
        self.heap.append(k)
        self.size = self.size + 1
        self.shiftUp(self.size)

    def shiftDown(self,i):
        if(2*i <= self.size):
            max = self.maxChild(i)
            if (max != i) and self.heap[i] < self.heap[max]:
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
    def extractMax(self):
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

def main():
    Heap = BinHeap()
    op = 0
    while(op != 6):
        print("1.Insert\n2.extract-Max\n3.showMax\n4.Build new Heap\n5.Heapsort\n6.Exit \n")
        op = int(input("Enter choice :"))
        if op == 1:
            temp=0
            temp=int(input("Enter Element : "))
            Heap.insert(temp)

        elif op == 2:
            print("Max was : " , Heap.extractMax())
        
        elif op == 3:
            print("Max is : " , Heap.heap[1])
        
        elif op == 4:
            print("enter new list")    
            Heap.buildHeap([int(x) for x in input().split()])
        elif op == 5:
            result=[]
            for i in range(0,Heap.size):
                result.append(Heap.extractMax())
            result.reverse()
            Heap.buildHeap(result)
            print(result)
    
if __name__ == '__main__':
    main()