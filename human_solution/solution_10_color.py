from collections import Counter

testCases = int(input())

for count in range(testCases):
	number = int(input())
	string = input()
	colors = Counter(string)
	print(number-max(colors.values()))
