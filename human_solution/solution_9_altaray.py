# /cc/2016/March/CookOff/ALTARAY

n_tests = eval(input())
for tc in range(n_tests):
	n_nums = eval(input())
	nums = list(map(int, input().strip().split()))
	las = [0] * n_nums
	las[n_nums - 1] = 1
	for i in range(n_nums - 2, -1, -1):
		las[i] = 1
		if (nums[i] / abs(nums[i])) * (nums[i + 1] / abs(nums[i + 1])) == -1:
			las[i] += las[i + 1]

	for num in las:
		print(num, end=' ')
	print()