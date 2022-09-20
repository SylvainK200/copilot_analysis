t=eval(input())
while(t>0):
	t-=1
	n=eval(input())
	if(360%n==0):
		print("y", end=' ')
	else:
		print("n", end=' ')
	if(n<=360):
		print("y", end=' ')
	else:
		print("n", end=' ')
	if(n*(n+1)<=720):
		print("y", end=' ')
	else:
		print("n", end=' ')
