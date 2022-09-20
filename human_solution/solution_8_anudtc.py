def check1 (n):
	if (360%n==0):
		print('y', end=' ')
	else:
		print('n', end=' ')
def check2 (n):
	if (n<=360):
		print('y', end=' ')
	else:
		print('n', end=' ')
def check3 (n):
	if ((n*(n+1))/2<=360):
		print('y')
	else:
		print('n')
t=int(input())
for asd in range (t):
	n=int(input())
	check1(n)
	check2(n)
	check3(n)