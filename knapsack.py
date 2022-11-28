a=[]
def knapSack(W, wt, val, n):
	if n == 0 or W == 0 :
		return 0
	if (wt[n-1] > W):
		a.clear()
		return knapSack(W, wt, val, n-1)
	else:
		a.append(val[n-1])
		return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
				knapSack(W, wt, val, n-1))

val = [3,4,5,6]
wt = [2, 3, 4,5]
W = 5
n = len(val)
print(knapSack(W, wt, val, n))
a.pop()
print(a)