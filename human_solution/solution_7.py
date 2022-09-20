def solve(s, nlen):
    indexes = [""] * nlen
    
    i = 0
    for si in s:
        for num in si:
            indexes[num] += ("," + str(i))
        i += 1

    indexes.sort()
    cur = indexes[0]
    i = 1
    dup_cnt = 0
    while i < n:
        if indexes[i] == cur:
            dup_cnt += 1
        else:
            cur = indexes[i]
        i += 1
    print((nlen - dup_cnt))

t = int(input())
while t > 0:
    (n, m) = (int(x) for x in input().split(' '))
    s = []
    for i in range(m):
        l = [int(x) for x in input().split(' ')]
        del l[0]
        s.append(l)
    solve(s, n)    
    t -= 1
