t=eval(input())
for i in range(t):
	n=eval(input())
	arr=list(map(int,input().split()))
	c=0
	for j in range(n):
		s=0
		p=1
		for k in range(j,n):
			s+=arr[k]
			p*=arr[k]
			if s==p:
				c+=1
	print(c) 