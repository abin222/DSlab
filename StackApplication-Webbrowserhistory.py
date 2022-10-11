class Webbrowser:
    def __init__(self,n):
        self.size=n
        self.data=[None]*self.size
        self.top=-1
        
    def LoadWebsite(self,url):
        self.push(url)
        
    def LoadRecent(self):
        e=self.tops()
        self.push(e)
        
    def deleteNhistories(self,n):
        while(n>-1 or self.isEmpty()==False):
            print(self.pop())    
        
    def historysize(self):
        return self.top+1
    
    def push(self,c):
        if(self.isFull()==False):
            self.top=self.top+1
            self.data[self.top]=c
        else:
            print("Stack is Full")

       
    def printStack(self):
        print("Stack",self.data)

    def pop(self):
        temp=None
        if (self.isEmpty()==False):    
            temp=self.data[self.top]      
            self.data[self.top]=None
            self.top=self.top-1
        return temp

    
    def tops(self):
        temp=None
        #print(self.data[self.top])
        if (self.isEmpty()==False):    
            temp=self.data[self.top]
       # print ("top:",temp)
        return temp

    
    def isEmpty(self):
        if(self.top<0):
            return True
        else:
            return False

    def isFull(self):
        if(self.top==self.size-1):
            return True
        else:
            return False

        


size=input("enter size:")
s=Webbrowser(int(size))
n=int(input("1-10:"))
line=[]
print("line:",line)

while(n>0):
    line=(input()).split(',')
    print(line)
    if(line[0]=="Push"):
        print("Push")
        s.push(line[1])
        # s.printStack()
    elif(line[0]=="Pop"):
        print(s.pop())
    elif(line[0]=="LW"):  #LW-Loadwebsite
        s.LoadWebsite(line[1])
        s.printStack()
    elif(line[0]=="LR"):  #LR-LoadRecent
        s.LoadRecent()
        s.printStack()
    elif(line[0]=="dN"):  #dN-delete N histories
        s.deleteNhistories(int(line[1]))
        s.printStack()
    elif(line[0]=="sh"):  #sh-size of the history
        print(s.historysize())
    elif(line[0]=="Print"):
        s.printStack()
     





