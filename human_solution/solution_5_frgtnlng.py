for i in range(eval(input())):
	n, k = list(map(int, input().split()))
	words = input().split()
	modlan = []
	for i in range(k):
		s = input().split()
		del s[0]
		modlan += s
	for word in words:
		if(word in modlan):
			print("YES", end=' ')
		else:
			print("NO", end=' ')
	print("")