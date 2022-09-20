for t in range(eval(input())):
	n=eval(input())
	l=list(map(int,input().split()))
	dp=[1]*n
	for i in range(n-2,-1,-1):
		if l[i+1] > 0 and l[i] < 0:
			dp[i]=1+dp[i+1]
		elif l[i+1] < 0 and l[i] > 0:
			dp[i]=1+dp[i+1]
		else:
			dp[i]=1
	for i in dp:
		print(i, end=' ')
	print()
