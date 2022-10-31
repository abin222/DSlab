# Question:Implement the binary tree with following operations
# 1-Postorder traversal output tree
# 2-find the depth of all leaf Nodes
# 3-find the subtree of  a given reference node
class EvalTree:

    class node:
        def __init__(self,data):
            self.element = data
            self.value = None
            self.parent = None
            self.lc = None  #leftchild
            self.rc = None  #rightchild
    def __init__(self):
        self.root = None
        self.id=0
    def constructtree(self,expr):
        i=0
        lc=None
        while i < len(expr):
            print(expr[i])
            if (lc==None):
               
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
              
            else:
                
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
                # print("ii=",i)
            i=i+1
            
    def inordertraversal(self,r):
        if(r!= None):
            #print("inordertraversal",r.element)
            self.inordertraversal(r.lc)
            print(r.element, end =" ")
            self.inordertraversal(r.rc)
    def findDepth(self,r,d):
        if(r!=None):
            if(r.lc==None and r.rc==None):
                print(r.element,"Depth:",d)
            d+=1
            self.findDepth(r.lc,d)
            self.findDepth(r.rc,d)
    def traverse(self,r):
         if(r!= None):
            print(r.element,"id:",self.id)
            self.id+=1
            self.traverse(r.lc)
            self.traverse(r.rc)
    def postordertraversal(self,r):
       if(r!= None):
            self.postordertraversal(r.lc)
            self.postordertraversal(r.rc)
            print(r.element, end =" ")
    def subTree(self,r,id):
        if(r!= None):
            if(self.id==id):
                print("Postorder:")
                self.postordertraversal(r)
            self.id+=1
            self.subTree(r.lc,id)
            self.subTree(r.rc,id)
		




def main():
    tree = EvalTree()
    expr=input("Enter the expersion: ")
    tree.constructtree(expr)
    tree.inordertraversal(tree.root)
    while True:
        print("\nMenu")
        print("1-find Depth")
        print("2-Post Order traversal")
        print("3-Sub Tree")
        print("4-Quit")
        operation=int(input("Your Choice:"))
        if(operation==2):
            tree.postordertraversal(tree.root)
        if(operation==1):
            tree.findDepth(tree.root,0)
        if(operation==3):
            tree.traverse(tree.root)
            val=int(input("Enter id:"))
            tree.id=0
            tree.subTree(tree.root,val)
        if(operation==4):
            break

if __name__ == '__main__':
    main()

