test = int(input())
for i in range(test):
	k = int(input())
	x = list(map(int , input().split()))
	no_stem = 0.5
	j=1
	while j<=k:
		no_stem = no_stem * 2 - x[j-1]
		j+=1
	if no_stem==0:
		print("Yes")
	else:
		print("No")