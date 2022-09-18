T = eval(input())
for i in range(T):
  	n, m = list(map(int, input().split()));
	mmin, mmax = n, -1
	x = list(map(int, input().split()))
	mmin = min(x)
	mmax = max(x)
	ans = [0] * n
	for j in range(n):
	  	ans[j] = max(abs(mmin - j), abs(mmax - j))
	print(' '.join(map(str, ans)))
