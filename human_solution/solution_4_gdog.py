testcases = int(input())

for i in range(0, testcases):
    inputarray = [int(x) for x in input().split()]
    n = inputarray[0]
    k = inputarray[1]
    coinsfordog = 0
    maxmod = 0
    for j in range(k,1,-1):
        if n % j < maxmod:
            break
        else:
            maxmod = n % j
    print(maxmod)