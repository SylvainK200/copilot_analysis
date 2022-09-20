t = eval(input())
while t > 0:
    n = eval(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = []
    c.append(a[0])
    for i in range(1,len(a)):
        c.append(a[i] - a[i-1])
    count = 0
    for i in range(len(a)):
        if c[i] >= b[i]:
            count = count + 1
    print(count)
    t = t-1