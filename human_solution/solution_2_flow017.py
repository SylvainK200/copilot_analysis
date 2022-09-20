t=int(eval(input()))
while t :
	a=input().split(' ')
	a=list(map(int,a))
	a.sort()
	print((a[1]))
	t=t-1 