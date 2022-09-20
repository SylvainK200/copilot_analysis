# I love GOD
t = int(input())
for i in range(t):
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(0, N):
        sum, pro = 0, 1
        for j in range(i, N):
            sum += a[j]
            pro *= a[j]
            if sum == pro: ans += 1
    print(ans)