# Circular Queue implementation in Python


class MyCircularQueue():

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    # Insert an element into the circular queue
    def enqueue(self, data):

        if ((self.tail + 1) % self.k == self.head):
            print("The circular queue is full\n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data
	# Insert an element into the circular queue from left
    def enqueueleft(self, data):

        if ((self.tail + 1) % self.k == self.head):
            print("The circular queue is full\n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.head = (self.head + 1) % self.k
            self.queue[self.head] = data
    # Delete an element from the circular queue from left
    def dequeueleft(self):
        if (self.head == -1):
            print("The circular queue is empty\n")

        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.tail = (self.tail + 1) % self.k
            return temp
    # Delete an element from the circular queue
    def dequeue(self):
        if (self.head == -1):
            print("The circular queue is empty\n")

        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

    def printCQueue(self):
        if(self.head == -1):
            print("No element in the circular queue")

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()


# Your MyCircularQueue object will be instantiated and called as such:
size=int(input("enter size:"))
obj = MyCircularQueue(size)
while(True):
    print("Menu")
    print("Enqueue-1")
    print("Dequeue-2")
    print("EnqueueLeft-3")
    print("Dequeueleft-4")
    print("Print CQueue-5")
    print("Quit-6")
    x=int(input("Choice:"))
    if(x==1):
        val=input("Enter the val:")
        obj.enqueue(val)
    if(x==5):
        print("queue:")
        obj.printCQueue()
    if(x==2):
        obj.dequeue()
        print("After removing an element from the queue")
        obj.printCQueue()
    if(x==3):
        val=input("Enter the val:")
        obj.enqueueleft(val)
    if(x==4):
        obj.dequeueleft()
        print("After removing an element from the queue")
        obj.printCQueue()
    if(x==6):
        break
        
