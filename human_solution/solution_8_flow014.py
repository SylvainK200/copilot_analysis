T = int(input())
for t in range(T):
	x, y,z = list(map(float,input().strip().split(' ')))
	x = int(x)
	z = int(z)
	if x > 50:
		f1 = 1
	else:
		f1 = 0
	if y < 0.7:
		f2 = 1
	else:
		f2 = 0
	if z > 5600:
		f3 = 1
	else:
		f3 = 0
	if f1 and f2 and f3:
		print(10)
	elif f1 and f2:
		print(9)
	elif f2 and f3:
		print(8)
	elif f1 and f3:
		print(7)
	elif f1 or f2 or f3:
		print(6)
	else:
		print(5)
	