import sys
def aprox(t):
	for i in range(t):
		n = int(sys.stdin.readline())
		if n == 0:
			print(3)
		else:
			u,d,s = 103993,33102,'3.'
			for j in range(n+1):
				s += str(u/d)
				u = u%d*10
			print(s[:2]+s[3:])
aprox(int(sys.stdin.readline()))