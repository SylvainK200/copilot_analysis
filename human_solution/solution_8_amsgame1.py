from fractions import gcd
from functools import reduce
for _ in range(eval(input())):
    n=eval(input())
    li=list(map(int,input().split()))
    print(reduce(gcd,li))
