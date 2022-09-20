t=int(input())
for i in range(0,t):
	n=int(input())
	lis1=list(map(int,input().split()))
	lis2=list(map(int,input().split()))
	count=0
	for j in range(0,n):
		if j==0:
			if lis2[j]<=lis1[j]:
				count+=1
		else:
			if lis1[j]-lis1[j-1] >= lis2[j]:
				count+=1
	print(count)