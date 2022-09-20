testcase = eval(input())
for i in range(0, testcase):
	x, y, z = list(map(int, input().split()))
	if(x == 0 or y == 0 or z == 0):
		print("NO")
	elif(x + y + z == 180):
		print("YES")
	else:
		print("NO")