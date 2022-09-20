import operator
from functools import reduce
t=int(input())
def prod(iterable):
    return reduce(operator.mul, iterable, 1)

for i in range(0,t):
	eval(input())
	a=list(map(int,input().split(" ")))
	print(len([a[k:k+i] for k in range(0,len(a)) for i in range(1,len(a)+1-k) if sum(a[k:k+i])==prod(a[k:k+i]) ]))
	

