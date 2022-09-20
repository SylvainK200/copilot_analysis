for n in range(int(input())):
	x,y = list(map(int, input().split()))
	z = 0;
	while x != y:
	   if x > y:
	      x = x/2
	   else:
	      y = y/2
	   z += 1
	print(z)