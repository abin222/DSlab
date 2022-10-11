class Variables:
    def __init__(self,n):
        self.size=n
        self.data=[None]*self.size
        self.top=-1
    def push(self,c):
        if(self.isFull()==False):
            self.top=self.top+1
            self.data[self.top]=c
        else:
            print("Stack is Full")

       
    def printStack(self):
        print("Variables ",self.data)

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
class ConverInPost:
 
    # Constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # This array is used a stack
        self.array = []
        # Precedence setting
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
 
    # check if the stack is empty
    def isEmpty(self):
        return True if self.top == -1 else False
 
    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]
 
    # Pop the element from the stack
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
 
    # Push the element to the stack
    def push(self, op):
        self.top += 1
        self.array.append(op)
 
    # A utility function to check is the given character
    # is operand
    def isOperand(self, ch):
        return ch.isalpha()
 
    # Check if the precedence of operator is strictly
    # less than top of stack or not
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False
 
    # The main function that
    # converts given infix expression
    # to postfix expression
    def infixToPostfix(self, exp):
 
        # Iterate over the expression for conversion
        for i in exp:
            # If the character is an operand,
            # add it to output
            if self.isOperand(i):
                self.output.append(i)
 
            # If the character is an '(', push it to stack
            elif i == '(':
                self.push(i)
 
            # If the scanned character is an ')', pop and
            # output from the stack until and '(' is found
            elif i == ')':
                while((not self.isEmpty()) and
                      self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()
 
            # An operator is encountered
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)
 
        # pop all the operator from the stack
        while not self.isEmpty():
            self.output.append(self.pop())
 
        return "".join(self.output)
        
# convert infix to prefix
class ConverInPre:
     # Constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # This array is used a stack
        self.array = []
        # Precedence setting
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    def isOperator(self,c):
        return (not (c >= 'a' and c <= 'z') and not(c >= '0' and c <= '9') and not(c >= 'A' and c <= 'Z'))
    # Function to find priority
	# of given operator.
    def getPriority(self,C):
        if (C == '-' or C == '+'):
            return 1
        elif (C == '*' or C == '/'):
            return 2
        elif (C == '^'):
            return 3
        return 0
    # Function that converts infix
    # # expression to prefix expression.
    def infixToPrefix(self,infix):
        		# stack for operators.
        operators = []
        
        operands = []
        for i in range(len(infix)):
            if (infix[i] == '('):
                operators.append(infix[i])
            elif (infix[i] == ')'):
                while (len(operators)!=0 and operators[-1] != '('):
                    op1 = operands[-1]
                    operands.pop()
                    op2 = operands[-1]
                    operands.pop()
                    op = operators[-1]
                    operators.pop()
                    tmp = op + op2 + op1
                    operands.append(tmp)
                operators.pop()
            elif (not self.isOperator(infix[i])):
                operands.append(infix[i] + "")
            else:
                while (len(operators)!=0 and self.getPriority(infix[i]) <= self.getPriority(operators[-1])):
                    op1 = operands[-1]
                    operands.pop()
                    op2 = operands[-1]
                    operands.pop()
                    op = operators[-1]
                    operators.pop()
                    tmp = op + op2 + op1
                    operands.append(tmp)
                operators.append(infix[i])
        while (len(operators)!=0):
            op1 = operands[-1]
            operands.pop()
            op2 = operands[-1]
            operands.pop()
            op = operators[-1]
            operators.pop()
            tmp = op + op2 + op1
            operands.append(tmp)
        return operands[-1]
class ConverPostIn:
        # Constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # This array is used a stack
        self.array = []
        # Precedence setting
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    def isOperand(self,x):
        return ((x >= 'a' and x <= 'z') or
            (x >= 'A' and x <= 'Z'))
    def getInfix(self,exp) :
        s = []
        for i in exp:
            if (self.isOperand(i)) :        
                s.insert(0, i)
            else:
                op1 = s[0]
                s.pop(0)
                op2 = s[0]
                s.pop(0)
                s.insert(0, "(" + op2 + i +
								op1 + ")")
        return s[0]
class ConverPreIn:
     # Constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # This array is used a stack
        self.array = []
        # Precedence setting
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    def prefixToInfix(self,prefix):
        stack = []
        i = len(prefix) - 1
        while i >= 0:
            if not self.isOperator(prefix[i]):
                stack.append(prefix[i])
                i -= 1
            else:
                str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
                stack.append(str)
                i -= 1
        return stack.pop()
    def isOperator(self,c):
        if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
            return True
        else:
            return False
class Evaluate:
     
    # Constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # This array is used a stack
        self.array = []
     
    # check if the stack is empty
    def isEmpty(self):
        return True if self.top == -1 else False
     
    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]
     
    # Pop the element from the stack
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
     
    # Push the element to the stack
    def push(self, op):
        self.top += 1
        self.array.append(op)
    #check if operand
    def isOperand(self,x):
        return ((x >= 'a' and x <= 'z') or
            (x >= 'A' and x <= 'Z'))
 
 
    # The main function that converts given infix expression
    # to postfix expression

    def evaluatePostfix(self, exp,varia):
         
        # Iterate over the expression for conversion
        for i in exp:
             
            # If the scanned character is an operand
            # (number here) push it to the stack
            if self.isOperand(i):
                self.push(i)
 
            # If the scanned character is an operator,
            # pop two elements from stack and apply it.
            else:
                val1 = self.pop()
                val2 = self.pop()
                varia.printStack()
                while(varia.isEmpty()==False):
                    data1=varia.pop()
                    if(val1==data1[0]):
                        val1=data1[1]
                    if(val2==data1[0]):
                        val2=data1[1] 
                                   
                if(i=="+"):
                    val=int(val1)+int(val2)
                if(i=="*"):
                    val=int(val1)*int(val2)
                if(i=='-'):
                    val=int(val2)-int(val1)
                if(i=='/'):
                    val=int(val1)/int(val2)
                    
                    
                self.push(val)
 
        return int(self.pop())
# Driver code
if __name__ == '__main__':
    #input init for program run without quiting
    n=int(input("1-10: "))
    # No of experssions
    sizeV=int(input("No. of Variables available: "))
    va=Variables(sizeV)
    while(va.isFull()==False):
        #input of Variables
        a=input("Variables[a-z]: ")
        val=input("Value: ")
        va.push([a,val])
    va.printStack()
    print("Menu")
    print("To enter infix experssion-1 ")
    print("To enter postfix experssion-2")
    print("To enter prefix experssion-3")
    x=input("Your Choice :")
    if(x=="1"):
        inexp=input("Infix expersion expersions like a+b only use variable declared above:")
        print("Menu")
        print("convert to postfix-1")
        print('convert to prefix-2')
        print('evaluate-3')
        y=input('Your choice :')
        if(y=="1"):
            inpos = ConverInPost(len(inexp))
            print(inpos.infixToPostfix(inexp))
        if(y=="2"):
             inpre=ConverInPre(len(inexp))
             inpre=inpre.infixToPrefix(inexp)
             print(inpre)
        if(y=="3"):
            inpos = ConverInPost(len(inexp))
            val=inpos.infixToPostfix(inexp)
            eval=Evaluate(len(val))
            print(eval.evaluatePostfix(val,va))
    if(x=="2"):
        postexp=input("Postfix expersion expersions like ab+ only use variable declared above:")
        print("Menu")
        print("conver to infix-1")
        print('convert to prefix-2')
        print('evaluate-3')
        ya=input('Your choice :')
        if(ya=="1"):
            posin=ConverPostIn(len(postexp))
            print(posin.getInfix(postexp.strip()))
        if(ya=="2"):
            posin=ConverPostIn(len(postexp))
            inpre=posin.getInfix(postexp.strip())
            inpre=ConverInPre(len(inexp))
            inpre=inpre.infixToPrefix(inexp)
            print(inpre)
        if(ya=="3"):
            eval=Evaluate(len(postexp))
            print(eval.evaluatePostfix(postexp,va))
    if(x=="3"):
        preexp=input("Prefix expersion expersions like +ab only use variable declared above:")
        print("Menu")
        print("conver to infix-1")
        print('convert to postfix-2')
        print('evaluate-3')
        yb=input('Your choice :')
        if(yb=="1"):
            prein=ConverPreIn(len(preexp))
            print(prein.prefixToInfix(preexp))
        if(yb=="2"):
            prein=ConverPreIn(len(preexp))
            inpost=prein.prefixToInfix(preexp)
            inpost=ConverInPost(len(inpost))
            print(inpos.infixToPostfix(inpost))
        if(yb=="3"):
            prein=ConverPreIn(len(preexp))
            inpost=prein.prefixToInfix(preexp)
            inpost=ConverInPost(len(inpost))
            postexp=inpost.infixToPostfix(inpost)
            eval=Evaluate(len(postexp))
            print(eval.evaluatePostfix(postexp,va))
  
    # while(n>0):