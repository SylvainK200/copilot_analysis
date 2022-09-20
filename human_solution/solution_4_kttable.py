n = int(input())

for i in range(n):
	s = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	
	for i in range(len(a)-1, 0,-1):
		a[i] -= a[i-1]
	ans = 0
	for i in range(s):
		ans += 1 if a[i] >= b[i] else 0
	print(ans)