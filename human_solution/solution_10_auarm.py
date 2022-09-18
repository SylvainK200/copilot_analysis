for _ in range(eval(input())):
	n,m = list(map(int,input().split()))
	arr = list(map(int,input().split()))
	min_,max_ = min(arr),max(arr)
	for i in range(n):
		print(max(abs(i-max_),abs(i-min_)), end=' ')

