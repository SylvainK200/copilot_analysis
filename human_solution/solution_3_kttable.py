T=int(input())

for i in range(T):
	n=int(input())
	a=input().split()
	b=input().split()
	a=[int(x) for x in a]
	b=[int(x) for x in b]
	count=0
	for i in range(len(a)):
		if i==0:
			if a[i]-0>=b[i]:
				count+=1
				continue
		if a[i]-a[i-1]>=b[i]:
			count+=1
	
	print(count)				
				