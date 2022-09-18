for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    p = list(map(int, input().split()))
    r = list(range(n - min(p)))
    o = min(p) * [0] + r
    l = list(range(max(p) + 1))[::-1]
    for i in range(len(l)):
        if l[i] > o[i]:
            o[i] = l[i]
        else:
            break
    for i in o: print(i, end=' ')
    print()