t = eval(input())
for _ in range(t):
    a, b = list(map(int, input().split()))
    count = 0
    while a & (a - 1):
        if a % 2:
            a = (a - 1) / 2
        else:
            a /= 2
        count += 1
    if a > b:
        while a != b:
            a /= 2
            count += 1
    elif a < b:
        while a != b:
            a *= 2
            count += 1
    print(count)
