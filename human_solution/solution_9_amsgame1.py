t=int(input())
while t>0:
	t-=1
	n=int(input())
	l=[int(x) for x in input().split()]
	while 1:
		m=min(l)
		if l.count(m)==n:
			break
		for i in range(n):
			if l[i]%m==0:
				l[i]=m
			else:
				l[i]=l[i]%m
	print(m)