# @author Kilari Teja
# FLOW017

for _ in range(int(input().strip())):
	Subjects = list(map(int, input().strip().split(" ")))
	Subjects.sort(reverse=True)
	print(Subjects[1])