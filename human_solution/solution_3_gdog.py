t = eval(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    print(max([n % i for i in range(1, k + 1)]))
