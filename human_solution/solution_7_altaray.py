# your code goes here
t = eval(input())
for i in range(t):
	n = eval(input())
	a = list(map(int,input().split()))
	z = [0]*n
	z[-1]=1
	k = n-1
	while k>0:
		if (a[k]<0 and a[k-1]<0) or (a[k]>0 and a[k-1]>0):
			z[k-1]=1
		else:
			z[k-1]=z[k]+1
		k-=1
	print(' '.join(map(str,z)))

	