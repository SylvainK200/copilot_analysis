test = eval(input())

while test>0 :

	test = test -1

	n=eval(input())
	count = 0

	temp = n/100
	count = count + temp
	n = n - temp*100

	temp = n/50
	count = count + temp
	n = n - temp*50

	temp = n/10
	count = count + temp
	n = n - temp*10

	temp = n/5
	count = count + temp
	n = n - temp*5

	temp = n/2
	count = count + temp
	n = n - temp*2

	temp = n/1
	count = count + temp
	n = n - temp*1

	print(count)