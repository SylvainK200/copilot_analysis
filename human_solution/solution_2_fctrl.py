testCases = int(input())
for x in range(testCases):
	num = int(input())
	zeroes = 0
	y = 5
	while num / y >= 1:
		zeroes += num / y
		y *= 5
	print(zeroes)