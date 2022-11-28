
def knapsack(W,n,I,w,b):
    v=[None]*n         #vi
    x=[None]*n         #xi
    i=0
    print(I) 
    while(i<n):
        x[i]=0
        v[i]=b[i]/w[i]
        print("v",b[i]/w[i])
        i=i+1
    print("V:",v)
    #sort I,x and v based on v
    #bubble sort
    i=0
    while(i<n):
       while(j<n):
           if(v[i]>v[j]):#swap
               temp=v[j]
               v[j]=v[i]
               v[i]=temp

               temp=b[j]
               b[j]=b[i]
               b[i]=temp
               
               temp=w[j]
               w[j]=w[i]
               w[i]=temp

               temp=I[j]
               I[j]=I[i]
               I[i]=temp
               
    print("Knapsack:")
    print("I:",I)
    print("w:",w)
    print("b:",b)
    print("v:",v)
    return(I,x,v)



##Input
W=int(input())#TotalCapacity
n=int(input())#number of items
I=[None]*n         #item number
w=[None]*n         #wi
b=[None]*n         #bi

i=0
print(I," ",len(I))
while (n>0):
    item=(input()).split()
    print(item[0]," ",item[1])
    I[i]=i
    w[i]=int(item[0])
    b[i]=int(item[1])
    i=i+1
    n=n-1
           
(Is,X,V)=knapsack(W,n,I,w,b)
