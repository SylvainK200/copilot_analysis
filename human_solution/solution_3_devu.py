for t in range(int(input())):
    (n, m), a = input().split(), input().split()
    n, m, result = int(n), int(m), 0
    for num in a:
        x = int(num)
        y = x % m
        result += m - y if x == y else min(y, m - y)
    print(result)