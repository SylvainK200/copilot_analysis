t=int(input())
while(t):
	n,k=list(map(int,input().split()))
	a=list(map(int,input().strip().split(" ")))
	ans=0
	small=2000000000
	for i in range(n):
		for j in range(i+1,n):
			if(abs(a[i]+a[j]-k)<small):
				small=abs(a[i]+a[j]-k)
				ans=1
			elif(abs(a[i]+a[j]-k)==small):
				ans+=1
	print(small,ans)	
	t-=1
