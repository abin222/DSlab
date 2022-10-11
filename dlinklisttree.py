class Tree:
    # Node definition
    class Node:
        def __init__(self,data,parent=None,Child1=None,Child2=None,):
            self.data=data
            self.parent=parent
            self.child1=Child1
            self.child2=Child2