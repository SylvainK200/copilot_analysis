t=int(eval(input()))
while t:
	n=int(eval(input()))
	count=1
	a=b=1
	while a+b <=n:
		c=a+b
		a=b
		b=c
		count+=1
	print(count)
	t-=1