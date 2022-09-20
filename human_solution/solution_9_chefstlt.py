t = int(input())
for _ in range(t):
    s = input()
    r = input()
    mn = 0
    mx = 0
    slen = len(s)
    for i in range(slen):
        if s[i] == '?' or r[i] == '?':
            mx += 1
        if s[i] != '?' and r[i] != '?' and s[i] != r[i]:
            mx += 1
            mn += 1
    print(mn, mx)