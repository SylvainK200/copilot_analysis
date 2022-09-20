tc = int(input())
while tc > 0:
    tc = tc - 1
    n, k = list(map(int, input().split()))
    ans = 0
    for i in range(1,k+1):
        ans = max(ans, n%i)
    print(ans)
