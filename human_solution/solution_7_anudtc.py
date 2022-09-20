test_case = int(input())
for t in range(test_case):
	n = int(input())
	if 360 % n == 0:
		print('y', end=' ')
	else:
		print('n', end=' ')
	if n <= 360:
		print('y', end=' ')
	else:
		print('n')
	if (n*(n+1)/2) <= 360:
		print('y', end=' ')
	else:
		print('n') 