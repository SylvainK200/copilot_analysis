test=int(input())
a=0
while(a<test):
	a=a+1
	b=list(map(int,input().split()))
	b=sorted(b)
	print(b[1])