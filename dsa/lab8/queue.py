class Queue: 
    def __init__(self, capacity): 
        self.front = self.size = 0
        self.rear = capacity -1
        self.Q = [None]*capacity 
        self.capacity = capacity 
        
    def isFull(self): 
        return self.size == self.capacity
    def isEmpty(self): 
        return self.size == 0

    def push(self, item): 
        if self.isFull(): 
            return
        self.rear = (self.rear + 1) % (self.capacity) 
        self.Q[self.rear] = item 
        self.size = self.size + 1
  
    def pop(self): 
        if self.isEmpty(): 
            return
        self.front = (self.front + 1) % (self.capacity) 
        self.size = self.size -1

    def peek(self): 
        if self.isEmpty(): 
            return
        return self.Q[self.front]

if __name__ == '__main__': 
  
    queue = Queue(30) 
    queue.push(10) 
    queue.push(20) 
    queue.push(30) 
    queue.push(40) 
    queue.pop() 
    queue.peek() 