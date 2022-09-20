T = eval(input())
for testcase in range(T):
	N = eval(input())
	normal = [int(time) for time in input().split(" ")]
	required = [int(time) for time in input().split(" ")]
	normal.insert(0,0)
	diff = [normal[i] - normal[i-1] for i in range(1, len(normal))]
	no = 0
	for i in range(len(required)):
		if required[i] <= diff[i]:
			no += 1
	print(no)