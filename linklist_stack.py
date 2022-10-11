# the node class is used to create an element holder and the respective reference pointers.
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# this is the main class that that is used to create queues data struture which contains many functions.
class Stack:
    # this is automatically class when an instance of the class is called.
    def __init__(self):
        self.top = None
    # the below function is used to append an value on the top of the stack.  
    def push(self, data):
        if self.top is None:
            self.top = Node(data, None)
            return
        self.top = Node(data, self.top)
    # the below function is used to remove an value from the top of the stack.
    def pop(self):
        if self.top is None:
            return
        temp = self.top
        if self.top is not None:
            self.top = self.top.next
        temp.next = None
        return temp.data
    # the below function returns the value on the top of the stack.  
    def peek(self):
        return self.top.data
    # this function simply clears the whole stack.
    def clearstack(self):
        self.top = None
    # the below tells us if the stack is empty.
    def emptystack(self):
        if self.top is None:
            return True
        return False
    # this below function is used print out the stacks.
    def display(self):
        itr = self.top
        sstr = ' '
        while itr:
            sstr += str(itr.data) + '-->'
            itr = itr.next
        print(sstr)

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.display()
    stack.push(20)
    stack.display()
    stack.push(40)
    stack.peek()
    stack.display()
    stack.pop()
    stack.display()
    stack.push(30)
    stack.display()
    stack.clearstack()
    stack.display()