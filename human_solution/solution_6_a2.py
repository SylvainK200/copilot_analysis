test = int(input())

for t in range(test):
	levels = int(input())
	maxleaf = 0.5
	leaf = list(map(int,input().split()))
	for i in range(levels):
		maxleaf = 2*maxleaf-leaf[i]
	
	print("Yes" if maxleaf==0 else "No")