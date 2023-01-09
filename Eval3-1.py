# minimum no of operations (insert/Delete/Replace) to convert string A=ABC to string B=AXBC
# k=0
def min_ops(A, B, i, j, dp):
	if i == 0:
		return j
	if j == 0:
		return i
	if dp[i][j] != -1:
		return dp[i][j]
	if A[i-1] == B[j-1]:
		dp[i][j] = min_ops(A, B, i-1, j-1, dp)
	else:
		# k=+1
		dp[i][j] = 1 + min(min_ops(A, B, i-1, j, dp), # remove operation
						min_ops(A, B, i, j-1, dp), # insert operation
						min_ops(A, B, i-1, j-1, dp)) # replace operation
	# print(i,',',j,':',dp[i][j])
	# print(k)
	return dp[i][j]

def main():
	
	A = "ABC"
	B = "xytC"
	n = len(A)
	m = len(B)
	dp = [[-1]*(m+1) for _ in range(n+1)]
	print("Minimum number of operations to convert A to B:", min_ops(A, B, n, m, dp))
	k=0
	for i in range(len(A)):
		for j in range(len(B)):
			if dp[i][j]!=-1:
				# print(dp[i][j])
				k=k+1
	# print(dp)
	print("subproblems:",k)
main()

# A=ABC
# B=AXBC
# min_ops(A,B,4,5,)
# A[3]=B[4]
# dp[4][5]=min_ops(A,B,3,4,)
# A[2]=B[3]
# dp[3][4]=min_ops(A,B,2,3,)
# A[1]!=B[2]
# dp[2][3]=1+min(min_ops(A,B,1,3,),min_ops(A,B,2,2,),min_ops(A,B,1,2,))
# 1+min(3,2,1)

