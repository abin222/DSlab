 #@start-editable@
class EvalTree:

    class node:
        def __init__(self,data):
            self.element = data
            self.value = None
            self.parent = None
            self.lc = None  #leftchild
            self.rc = None  #rightchilds
            
    def __init__(self):
        self.root = None
        
    def constructtree(self,expr):
        i=0
        lc=None
        while i < len(expr):
            print(expr[i])
            if (lc==None):
                print("lc isnone")
                lc=self.node(expr[i])
                i=i+1
                op=self.node(expr[i])
                i=i+1
                rc=self.node(expr[i])
                op.lc=lc
                op.rc=rc
                op.parent=None
                lc.parent=op
                rc.parent=op
                self.root=op
                print("i=",i)
            else:
                print("lc is not none")
                lc=op
                op=self.node(expr[i])
                i=i+1
                rc=self.node(expr[i])
                op.parent=None
                op.lc=lc
                op.rc=rc
                lc.parent=op
                rc.parent=op
                self.root=op
                print("ii=",i)
            i=i+1
            
    def inordertraversal(self,r):
        if(r!= None):
            #print("inordertraversal",r.element)
            self.inordertraversal(r.lc)
            print(r.element, end =" ")
            self.inordertraversal(r.rc)
    
    def postordertraversal(self,r):
       if(r!= None):
            #print("Postordertraversal",r.element)
            self.postordertraversal(r.lc)
            self.postordertraversal(r.rc)
            print(r.element, end =" ")
            
    def readValuesfromuser(self,r):
        if(r.lc==None and r.rc==None):
            print("Enter the value for",r.element,":")
            r.value=int(input())
        else:
            self.readValuesfromuser(r.lc)
            self.readValuesfromuser(r.rc)
        
    def evaluatetree(self,r):
        #@start-editable@

       if(r!= None):
            #print("inordertraversal",r.element)
            l_value=self.evaluatetree(r.lc)
            r_value=self.evaluatetree(r.rc)
            if(r.element=='+'):
                r.value=l_value+r_value
            elif(r.element=='-'):
                r.value=l_value-r_value
            elif(r.element=='*'):
                r.value=l_value*r_value
            elif(r.element=='/'):
                r.value=l_value/r_value
            return r.value
       else:
            return None
        #@end-editable@


 
    def printList(self):
        if (self.size()==0):
            print ("List Empty")
        else:
            tnode = self.head
            while tnode!= None:
                print(tnode.element,end="->")
                tnode = tnode.next
            print("null")
        return


def testSLL():
    tree = EvalTree()
    n=int(input())#no. of of operations
    while n>0:
        print("n>0")
        command=input()
        operation=command.split()
        if(operation[0]=="IE"):
            tree.constructtree(operation[1])
            tree.inordertraversal(tree.root)
            print("\nPostorder")
            tree.postordertraversal(tree.root)
            
        elif(operation[0]=="E"):
            tree.readValuesfromuser(tree.root)
            print("Value of Expression:",tree.evaluatetree(tree.root))
        n-=1


def main():
      testSLL()


if __name__ == '__main__':
    main()
#@end-editable@
