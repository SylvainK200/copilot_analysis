t=int(input())
for i in range(0,t):
	lis=list(map(int,input().split()))
	n=lis[0]
	k=lis[1]
	lis1=list(map(int,input().split()))
	count = 0
	for j in range(0,n):
		x=lis1[j]
		mod = x%k
		if x<k:
			count+=(k-x)
		else:
			count+=min(mod,k-mod)
	print(count)