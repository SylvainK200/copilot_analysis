t = int(input())
for _ in range(t):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    res = 0
    for i in a:
        z = i%k
        y = k - z
        if i >= k:
            res += min(z, y)
        else:
            res += y
    print(res)
 