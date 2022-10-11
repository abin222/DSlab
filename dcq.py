# Python implementation of De-queue using circular
# array

# A structure to represent a Deque
MAX = 100


class Deque:
	def __init__(self, size):
		self.arr = [0] * size
		self.front = -1
		self.rear = 0
		self.size = size

	''' Operations on Deque:
	void insertfront(int key);
	void insertrear(int key);
	void deletefront();
	void deleterear();
	bool isFull();
	bool isEmpty();
	int getFront();
	int getRear(); '''

	# Checks whether Deque is full or not.
	def isFull(self):
		return ((self.front == 0 and self.rear == self.size-1) or self.front == self.rear + 1)

	# Checks whether Deque is empty or not.

	def isEmpty(self):
		return (self.front == -1)

	# Inserts an element at front
	def insertfront(self, key):

		# check whether Deque if full or not
		if (self.isFull()):
			print("Overflow")
			return

		# If queue is initially empty
		if (self.front == -1):
			self.front = 0
			self.rear = 0

		# front is at first position of queue
		elif (self.front == 0):
			self.front = self.size - 1

		else: # decrement front end by '1'
			self.front = self.front-1

		# insert current element into Deque
		self.arr[self.front] = key

	# function to inset element at rear end
	# of Deque.

	def insertrear(self, key):
		if (self.isFull()):
			print(" Overflow")
			return

		# If queue is initially empty
		if (self.front == -1):
			self.front = 0
			self.rear = 0

		# rear is at last position of queue
		elif (self.rear == self.size-1):
			self.rear = 0

		# increment rear end by '1'
		else:
			self.rear = self.rear+1

		# insert current element into Deque
		self.arr[self.rear] = key

	# Deletes element at front end of Deque

	def deletefront(self):
		# check whether Deque is empty or not
		if (self.isEmpty()):
			print("Queue Underflow")
			return

		# Deque has only one element
		if (self.front == self.rear):
			self.front = -1
			self.rear = -1

		else:
			# back to initial position
			if (self.front == self.size - 1):
				self.front = 0

			else: # increment front by '1' to remove current
				# front value from Deque
				self.front = self.front+1

	# Delete element at rear end of Deque

	def deleterear(self):
		if (self.isEmpty()):
			print(" Underflow")
			return

		# Deque has only one element
		if (self.front == self.rear):
			self.front = -1
			self.rear = -1

		elif (self.rear == 0):
			self.rear = self.size-1
		else:
			self.rear = self.rear-1

	# Returns front element of Deque

	def getFront(self):
		# check whether Deque is empty or not
		if (self.isEmpty()):
			print(" Underflow")
			return -1

		return self.arr[self.front]

	# function return rear element of Deque

	def getRear(self):
		# check whether Deque is empty or not
		if(self.isEmpty() or self.rear < 0):
			print(" Underflow")
			return -1

		return self.arr[self.rear]


# Driver code
if __name__ == "__main__":
	dq = Deque(5)
	while(True):
		print(f"Queue:{dq.arr}")
		print("Menu")
		print("Add Data to rear-1")
		print("Add Data to front-2")
		print("Remove Data from rear-3")
		print("Remove data from front-4")
		print("Get front and rear-5")
		print("Quit-6")
		x=int(input("Your Choice:"))
		if x==1:
	# Append to the rear
			a=input("Data you want to enter the rear side of queue: ")
			print("Adding to the rear: ")
			dq.insertrear(a)
		
		if x==2:
	# append to the front
			b=input("Data you want to enter the front side of queue: ")
			print("Adding to the front: ")
			dq.insertfront(b)

		    
		if x==3:
			# Remove from the rear
			print("Removing from the rear: ")
			dq.deleterear()
		
		if x==4:
			# Remove from the front
			print("Removing from the front: ")
			dq.deletefront()
		
		if x==5:
			
	#  front and rear element
			print("Get the front and rear element: ")
			print(f"get rear element : {dq.getRear()}")
			print(f"front element new front become : {dq.getFront()}")
		if x==6:
			break
	# Function calls

