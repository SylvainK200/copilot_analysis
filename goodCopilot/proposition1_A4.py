t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    n = n ** n
    print(str(n)[:k], str(n)[-k:])
    