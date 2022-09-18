t = int(input())
for i in range(t):
    n, m, k = map(int, input().split())
    if n-m > k:
        print(n-m-k)
    else:
        print(0)