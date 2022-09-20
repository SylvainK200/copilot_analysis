T = eval(input())
for i in range(T):
	row1 = input()
	row2 = input()
	diff_mirror = ""
	for i in range(len(row1)):
		if row1[i] == row2[i]:
			if row1[i] == "W":
				diff_mirror += "B"
			else:
				diff_mirror += "W"
		else:
			diff_mirror += "B"
	print(diff_mirror)