import sys

t = eval(input())
for i in range(t):
	k = eval(input())
	n = 4687
	d = 33102
	pi = '3'
	if k!=0:
		pi+='.'
		for i in range(k):
			n*=10
			pi+=str(n/d)
			n=n%d
	print(pi)