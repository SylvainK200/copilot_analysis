from collections import Counter
import sys

def main():
	from sys import stdin, stdout
	for count in range(int(stdin.readline())):
		number = int(stdin.readline())
		string = stdin.readline()
		colors = Counter(string)
		stdout.write(str(number-max(colors.values()))+'\n')

if __name__ == "__main__":
    main()
