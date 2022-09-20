from functools import reduce
t = int(eval(input()))
for test in range(t):
    raw = input().split()
    n,k = int(raw[0]),int(raw[1])
    print(reduce(lambda x,y: max(x,y),([n%x for x in range(1,k+1)])))