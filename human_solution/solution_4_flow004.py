n = int(input())

for i in range(n):
	key = int(input())
	last = key%10
	reverse = 0
	while key:
		reverse = reverse*10 + key%10
		key /= 10
	first = reverse%10
	print(first + last)