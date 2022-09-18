import math
output = list()
prime = list()
val = input()
t = int(val)
for i in range(t) :
	nums = list()
	string1 = input()
	nums = string1.split()
	a = float(nums[0])
	b = float(nums[1])
	output.append(a+b-1)
for i in range(t) :
	print(output[i])