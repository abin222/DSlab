class Tree:
    # Node definition
    class Node:
        def __init__(self,data):
            self.data=data
            self.parent=None
            self.lc=None     #left child
            self.rc=None #right child
    def __init__(self):
        self.root =None
    def constructttree(self,expr):
        i=0
        lc=None
        while i< len(expr):
            print(expr[i])
            if lc==None:
                print("lc is none")
                lc=self.Node(expr[i])
                i+=1
                op=self.Node(expr[i])
                i+=1
                rc=self.Node(expr[i])
                op.lc=lc
                op.rc=rc
                op.parent=None
                lc.parent=op
                rc.parent=op
                self.root=op
                print("i=",i)
            else:
                print("lc id not none")
                lc=op
                op=self.Node(expr[i])
                i+=1
                rc=self.Node(expr[i])
                op.parent=None
                op.lc=lc
                op.rc=rc
                lc.parent=op
                rc.parent=op
                self.root=op
                print("ii=",i)
            i+=1
    def traverseTree(self,root):
         if root.data:
             print(self.traverseTree(root.lc))
             print(root.data)
             print(self.traverseTree(root.rc))
if __name__ == "__main__":
	tree=Tree()
	tree.constructttree("a+b*c/d")
	# print(tree.root.data)
	tree.traverseTree(tree.root)
             
        
