T = eval(input())
for test in range(T):
	l = []
	N = list(map(int, input().split()))
#	sorted_values = sorted(N)
#	print sorted_values[1]


	N.remove(max(N))
	print(max(N))
