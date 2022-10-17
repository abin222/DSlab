# Implement evaluation of expression using tree and stack data structures with the following operations:

# # Construct the tree from the given expression string Assign the values to variables

#  #  # For each leaf node, prompt the user to enter the value

# # Evaluate the expression with suitable traversal Find the height of the tree

# # List of the leaf nodes

# # Merge two expression trees and evaluate
# Node:
	# Data-Operator /operand(eg:A,+)
	# Value-for the operand(10)
	# Pointer to left child
	# Pointer to right child
    # POinter to parent
    
    
class Tree:
    # Node definition
    class Node:
        def __init__(self,data,val):
            self.data=data
            self.value=val
            self.parent=None
            self.lc=None     #left child
            self.rc=None #right child
    def __init__(self):
        self.root =None
    def constructttree(self,expr):
        i=0
        lc=None
        a=0
        b=0
        c=0
        while i< len(expr):
            print(expr[i])
            if lc==None:
                print("lc is none")
                # a=input("Enter value "+expr[i]+":")
                lc=self.Node(expr[i],a)
                i+=1
                op=self.Node(expr[i],b)
                
                i+=1
                # c=input("Enter value "+expr[i]+":")
                rc=self.Node(expr[i],c)
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
                if expr[i]=="a-z":
                    a=input("Enter value "+expr[i]+":")
                op=self.Node(expr[i],a)
                i+=1
                if expr[i]=="a-z":
                    b=input("Enter value "+expr[i]+":")
                rc=self.Node(expr[i],b)
                op.parent=None
                op.lc=lc
                op.rc=rc
                lc.parent=op
                rc.parent=op
                self.root=op
                print("ii=",i)
            i+=1
    def InordertraverseTree(self,root):
         if root is not None:
             self.InordertraverseTree(root.lc)
             print(root.data,end="")
             self.InordertraverseTree(root.rc)
    def PostordertraverseTree(self,root):
         if root is not None:
             self.PostordertraverseTree(root.lc)
             self.PostordertraverseTree(root.rc)
             print(root.data,end="")
    def PreordertraverseTree(self,root):
         if root is not None:
             print(root.data,end="")
             self.PreordertraverseTree(root.lc)
             self.PreordertraverseTree(root.rc)
if __name__ == "__main__":
	tree=Tree()
	tree.constructttree("a+b*c/d")
	# print(tree.root.data)
	print("\n InOrder\n")
	tree.InordertraverseTree(tree.root)
	print("\n Post Order\n")
	tree.PostordertraverseTree(tree.root)
	print("\n Preorder \n")
	tree.PreordertraverseTree(tree.root)
	print("\n")
             
        
