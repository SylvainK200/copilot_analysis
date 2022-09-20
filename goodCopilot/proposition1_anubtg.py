t = int(input())

for _ in range(t):
    n = int(input())
    costs = list(map(int, input().split()))
    costs.sort(reverse=True)
    total = 0
    for i in range(n):
        if i % 4 < 2:
            total += costs[i]
    print(total)