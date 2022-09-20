# cook your code here
test= int(input())
while(test>0):
	test-=1
	n=int(input())
	count=0
	i=0
	while(True):
		i=i+1
		k=n/pow(5,i)
		if (k>0):
			count=count+k
		else:
			break
	print(count)