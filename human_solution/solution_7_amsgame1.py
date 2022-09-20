from fractions import gcd
from functools import reduce
t = int(eval(input()))
for test in range(t):
	n = int(eval(input()))
	inp = list(map(int,input().split()))
	print(reduce(gcd,inp)) 