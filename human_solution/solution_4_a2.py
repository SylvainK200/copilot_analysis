def tree():
	levels = int(input())
	leaf = []
	cnt = 0.5
	leaf[0:] = list(map(int,input().split()))
	for i in range(len(leaf)):
		cnt = 2*cnt-leaf[i]
		if (cnt<0):
			break
	return cnt==0

test = int(input())
for t in range(test):
	if tree():
		print("Yes")
	else:
		print("No")