# Implement the Linked List with the following functions:

# a. Function to return the number of elements with O(1) complexity

# b. Function to print the last element with O(1) complexity 
# c. Function to enqueue front with O(1) complexity

# d. Function to remove the even elements (refers the positions) with O(n/2 complexity)
# the node class is used to create an element holder and the respective reference pointers.
 
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data #creating a storage for assigning value
        self.next = next #pointer to the next value
        self.prev = prev #pointer to the already existing previous value.
# this is the main class that that is used to create queues data struture which contains many functions.
class Queue:
    # this is automatically class when an instance of the class is called.
    def __init__(self): 
        self.front = self.rear = None
        self.size=0
    # this below function is used to append a value at the end of the queue which is similar to a late comer joins at the end.  
    def enqueue(self, data):
        if self.rear is None:
            self.front = self.rear = Node(data, None)
            return

        self.rear.next = Node(data, None)
        self.rear.next.prev = self.rear
        self.rear = self.rear.next
        self.size += 1
    # this below function is used remove a value from the start of the queue.
    def dequeue(self):
        if self.front is None:
            raise Exception('empty queue')
        temp = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
            return
        self.front.prev = None

        return temp
    # this code is used to clear the whole queue
    def clearqueue(self):
        self.front = self.rear = None
    # this is used to check idf the queue in empty or not.
    def emptyqueue(self):
        if self.front is None:
            return True
        return False
    # this is used to print queues
    def display(self):
        itr = self.front
        sstr = ' '
        while itr:
            sstr += str(itr.data) + '-->'
            itr = itr.next
        print(sstr)
    # Size of data
    def sizeof(self):
        return self.size
	
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.display()
    queue.enqueue(20)
    queue.display()
    queue.enqueue(30)
    queue.display()
    queue.dequeue()
    queue.display()
    queue.dequeue()
    queue.display()
    queue.dequeue()
    queue.display()
    queue.enqueue(40)
    queue.display()
    queue.enqueue(50)
    queue.display()
    queue.enqueue(60)
    queue.display()
    print("size of:")
    queue.sizeof()