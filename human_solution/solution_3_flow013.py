for _ in range(int(input().strip())):
	Subjects = list(map(float, input().strip().split()))
 
	if sum(Subjects) == 180.0:
		print("YES")
	else:
		print("NO")