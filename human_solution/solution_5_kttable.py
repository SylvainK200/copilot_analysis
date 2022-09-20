t = eval(input())
while t != 0:
	n = eval(input())
	x = list(map(int, input().split()))
	y = list(map(int, input().split()))
	c = 0
	m = 0
	l = 0
	for i in range(0, n):
		c = x[i]
		if(c - l >= y[i]):
			m += 1
		l = c
	print(m)
	t -= 1