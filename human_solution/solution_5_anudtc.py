t = int(input())

for T in range(t):
	n = int(input())

	if n <= 360 and 360%n == 0:
		print(("y "), end=' ')
	else:
		print(("n "), end=' ')
	
	if n <= 360:
		print(("y "), end=' ')
	else:
		print(("n "), end=' ')

	if 360 >= ((n+1)*n)/2:
		print("y ")
	else:
		print("n ")
