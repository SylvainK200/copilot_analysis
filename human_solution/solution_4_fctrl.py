t = int(input())
for i in range(t):
	temp = int(input())
	count = 0
	i = 5
	while(temp/i >0):
		count+=temp/i
		i=i*5

	print(count)
