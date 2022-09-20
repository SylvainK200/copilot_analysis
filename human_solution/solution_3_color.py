from collections import Counter

def output():
	for count in range(int(input())):
		number = int(input())
		string = input()
		colors = Counter(string)
		print(number-max(colors.values()))

output()
