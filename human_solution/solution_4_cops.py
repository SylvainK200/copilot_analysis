t = int(input())
for _ in range(t):
    h = [0]*101
    m,x,y = list(map(int, input().split()))
    z = x*y
    w = list(map(int, input().split()))
    for c in w:
        k = c
        while k < 101 and k <= (c+z):
            h[k] = 1
            k += 1
        k = c
        while k > 0 and k >= (c-z):
            h[k] = 1
            k -= 1
    res = 0
    for i in range(1, 101):
        if h[i] == 0:
            res += 1
    print(res)
