t=eval(input())
while t>0:
	t=t-1
	n=list(map(int,input().split()))
	print(abs(n[0]+n[1])-1)