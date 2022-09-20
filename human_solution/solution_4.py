import sys


testcases = int(sys.stdin.readline())

for x in range(testcases):
    sets = {}
    nm = list(map(int,sys.stdin.readline().split()))
    i = []
    for y in range(nm[1]):
        tempd = {}
        temparr = list(map(int, sys.stdin.readline().split()))
        for z in temparr[1:]:
            tempd[z] = 1
        i.append(tempd)
    for a in range(nm[0]):
        b = []
        for c in range(len(i)):
            if (a in i[c]):
                b.append(c)
        b.sort()
        sets[tuple(b)] = 1
    print(len(sets))






