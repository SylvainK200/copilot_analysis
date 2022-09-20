t = eval(input())
for i in range(t):
    n, k = list(map(int, input().split()))
    forgot, modern = [], []
    forgot = list(map(str, input().split()))
    for i in range(k):
        modern += list(map(str, input().split()))
    out = ""
    for x in forgot:
        if x in modern:
            out += "YES "
        else:
            out += "NO "
    print(out[0:-1])