t = int(input())
for i in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	ans = [None]*(n)
	a.insert(n, 0)
	for j in range(n-1, -1, -1):
		temp = a[j]*a[j+1]
		if temp < 0:
			ans[j] = ans[j+1] + 1;
			#print ans[j]
		else:
			ans[j] = 1
		#a[j] = a[j]*a[j+1]
	for j in range(n) : print(str(ans[j]), end=' ') 
	print() 
	