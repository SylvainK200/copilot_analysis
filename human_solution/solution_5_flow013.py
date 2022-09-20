def ValidTriangle(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return "NO"
    elif a+b+c == 180:
        return "YES"
    else:
        return "NO"

cases = int(input())
for i in range(cases):
    a, b, c = list(map(int, input().split()))
    print(ValidTriangle(a, b, c))