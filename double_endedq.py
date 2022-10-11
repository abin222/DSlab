import collections

DoubleEnded = collections.deque([])
if __name__ == "__main__":
    # Create a deque
    while(True):
        print("Menu")
        print("Add Data to right-1")
        print("Add Data to left-2")
        print("Remove Data from right-3")
        print("Remove data from left-4")
        print("Reverse Queue-5")
        print("Quit-6")
        x=int(input("Your Choice:"))
        if x==1:
# Append to the right
            a=input("Data you want to enter the right side of queue: ")
            DoubleEnded.append(a)
            print("Adding to the right: ")
            print(DoubleEnded)
        if x==2:
# append to the left
            b=input("Data you want to enter the left side of queue: ")
            print("Adding to the left: ")
            DoubleEnded.appendleft(b)
            print(DoubleEnded)    
        if x==3:
            # Remove from the right
            print("Removing from the right: ")
            DoubleEnded.pop()
            print(DoubleEnded)
        if x==4:
            # Remove from the left
            print("Removing from the left: ")
            DoubleEnded.popleft()
            print(DoubleEnded)
        if x==5:
            
# Reverse the dequeue
            print("Reversing the deque: ")
            DoubleEnded.reverse()
            print(DoubleEnded)
        if x==6:
            break
      