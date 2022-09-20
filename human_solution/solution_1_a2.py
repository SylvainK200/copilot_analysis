test = int(input())

for t in range(test):
	levels = int(input())
	maxleaf = 0.5
	leaf = list(map(int,input().split()))
	for i in range(levels):
		maxleaf = 2*maxleaf-leaf[i]
	
	if maxleaf==0:
		print("Yes")
	else:
		print("No")