import sys
t = int(input())
for i in  range(0,t):
	a,b,c = list(map(int,sys.stdin.readline().split()))
	if a > b:
		if b >c:
			print(b)
		else:
			if c > a:
				print(a)
			else:
				print(c)	
	else:
		if b < c:
			print(b)
		else:
			if c > a:
				print(c)
			else:
				print(a)				