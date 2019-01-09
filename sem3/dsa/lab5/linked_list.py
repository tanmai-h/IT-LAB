class ListNode:
    """Represents a node of a Singly Linked List.

    attributes: value, next. 
    """
    def __init__(self,val = None,nxt = None):
        self.value = val
        self.next = nxt

class LinkedList:
    """Defines a Singly Linked List.

    attributes: head
    """
    def __init__(self):
        """Create a new list with a Sentinel Node"""
        self.head = ListNode()
        self.length = 0

    def insert(self,x,pos):
        """Insert element x in the position after pos"""
        temp = ListNode(x,pos.next)
        pos.next = temp

    def delete(self,pos):
        """Delete the node following node pos in the linked list."""
        pos.next=pos.next.next

    def print(self):
        """ Print all the elements of a list in a row."""
        t = self.head.next
        l = []
        while t is not None:
            l.append(t.value)
            t = t.next
        return l

    def insertAtIndex(self,x,i):
        """Insert value x at list position i. (The position of the first element is taken to be 0.)"""
        t = self.head
        j = 0
        while j < i and t is not None:
            t = t.next
            j += 1

        if t is not None or j == 0:
            self.insert(x, t)
        else:
            print(j, " cant insert, out of range")

    def search(self, x):
        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
        t = self.head.next
        f = 0
        while(t is not None):
            if t.value == x:
                f = 1
                break
            t = t.next
        if f is 1:
            return True
        else:
            return False

    def isEmpty(self):
        "Return True if the Linked List has no elements, False otherwise."
        if(self.head.next is None):
            return True
        else:
            return False

    def len(self):
        "Return the length (the number of elements) in the Linked List."
        i = 0
        pos = self.head.next
        while(pos is not None):
            i += 1
            pos = pos.next
        return i

def main():
    L = LinkedList()
    L.insert(10,L.head)
    print('List is: ',L.print())
    L.insert(12,L.head.next)

    print('List is: ',L.print())
    L.insert(2,L.head)
    print('List is: ',L.print())
    print('Size of L is ',L.len())
    L.delete(L.head)
    print('List is: ',L.print())
    L.delete(L.head.next)
    print('List is: ',L.print())
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    L.delete(L.head)
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    L.insertAtIndex(2,0)
    L.insertAtIndex(1,0)
    L.insertAtIndex(4,2)
    L.insertAtIndex(3,2)
    print("Search: ", L.search(2))
    print('List is: ',L.print())

if __name__ == '__main__':
    main()