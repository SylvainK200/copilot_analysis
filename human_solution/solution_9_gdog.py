for i in range(0,int(input())):
	n,k = list(map(int,input().split()))
	max = 0
	k+=1
	for j in range(2,k):
		if n % j > max:
			max = n % j
	print(max)