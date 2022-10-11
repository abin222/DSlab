class Queue:
 
    # To initialize the object.
    def __init__(self, c):
 
        self.queue = []
        self.front = self.rear = 0
        self.capacity = c
        self.id=1
 
    # Function to insert an element
    # at the rear of the queue
    def queueEnqueue(self,id, name,addrs):
 
        # Check queue is full or not
        if(self.capacity == self.rear):
            print("\nQueue is full")
 
        # Insert element at the rear
        else:
            self.queue.append([id,name,addrs])
            self.queueDisplay()
            self.rear += 1
            
 
    # Function to delete an element
    # from the front of the queue
    def queueDequeue(self):
 
        # If queue is empty
        if(self.front == self.rear):
            print("Queue is empty")
 
        # Pop the front element from list
        else:
            x = self.queue.pop(0)
            self.queueDisplay()
            self.rear -= 1
		
			
    # Function to print queue elements
    def queueDisplay(self):
 
        if(self.front == self.rear):
            print("\nQueue is Empty")
 
        # Traverse front to rear to
        # print elements
        for i in self.queue:
            print(i, "<--", end='')
        print("\n")
 
    # Print front of queue
    def queueFront(self):
        if(self.front == self.rear):
            print("\nQueue is Empty")
 
        return self.queue[self.front]
        
        
    def cancelTic(self,can_id):
        print(can_id)
        if(self.front == self.rear):
            print("\nQueue is Empty")
            return
        e=0
        while True:
            i=self.queueFront()
            print(i[0])
            if int(i[0]) == int(can_id):
                print("correct")
                self.queueDequeue()
                break
            else:
                print("not correct",i)
                self.queueDequeue()
                self.queueEnqueue(i[0],i[1],i[2])
            e+=1
            if int(e)==int(self.capacity):
                break
            
        # self.queue.pop(self.rear)
class Wait:
	def __init__(self, c):

		self.queue = []
		self.front = self.rear = 0
		self.capacity = c

	# Function to insert an element
	# at the rear of the queue
	def queueEnqueue(self, name,addrs):

		# Check queue is full or not
		if(self.capacity == self.rear):
			print("\nQueue is full")

		# Insert element at the rear
		else:
			self.queue.append([name,addrs])
			self.rear += 1

	# Function to delete an element
	# from the front of the queue
	def queueDequeue(self):

		# If queue is empty
		if(self.front == self.rear):
			print("\n Waiting Queue is empty")

		# Pop the front element from list
		else:
			
			x = self.queue.pop(0)
			self.rear -= 1
			return x
		
			
	# Function to print queue elements
	def queueDisplay(self):

		if(self.front == self.rear):
			print("\nQueue is Empty")

		# Traverse front to rear to
		# print elements
		for i in self.queue:
			print(i, "<--", end='')

	# Print front of queue
	def queueFront(self):

		if(self.front == self.rear):
			print("\nQueue is Empty")

		print("\nFront Element is:",
				self.queue[self.front])
# Driver code
if __name__ == '__main__':
 
    # Create a new queue of
    # capacity 4
	n=int(input("1-10: "))
	size=int(input("No. of Seats available in reserved: "))
	q = Queue(size)
	wsize=int(input("No. of Seats available in waiting list: "))
	w = Wait(size)
    # Print queue elements
	q.queueDisplay()
	while(n>0):
		if(q.rear != size and w.front!=w.rear):
			x=w.queueDequeue()
			name=x[0]
			addrs=x[1]
			print(name)
			w.queueDequeue()
			q.queueEnqueue(q.id,name,addrs)
			q.id+=1
		print('\nMenu')
		print('Reserve Ticket-1')
		print('cancel ticket-2')
		print('add to waiting list-3')
		print('display the list-4')
		menuselect=input('Choose: ')
		if(menuselect=="1"):
			name=input('Name: ')
			addrs=input('Address: ')
    		# Inserting elements in the queue
			q.queueEnqueue(q.id,name,addrs)
			print('Your id is',q.id)
			q.id+=1	
			q.queueDisplay()

		if(menuselect=='2'):
			can_id=input('ID: ')
			q.cancelTic(can_id)
			q.queueDisplay()
			w.queueDisplay()
		if(menuselect=='3'):
			name=input('Name: ')
			addrs=input('Address: ')
    		# Inserting elements in the queue
			w.queueEnqueue(name,addrs)
			q.queueDisplay()
			w.queueDisplay()
		if(menuselect=='4'):
			q.queueDisplay()
			w.queueDisplay()	