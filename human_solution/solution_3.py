cases = int(input())

union_find = []

def find(v):
    if v == union_find[v]: return v
    return find(union_find[v])

def union(u, v):
    global union_find
    union_find[find(v)] = find(u)


for _ in range(cases):
    n,m = list(map(int, input().split()))
    setsmap = [0 for i in range(n)]
    union_find = [i for i in range(n)]
    for setindex in range(m):
        S = list(map(int, input().split()[1:]))
        for i in S:
            setsmap[i] |= (1<<setindex)
    
    for i in range(n):
        for j in range(i+1,n):
            if setsmap[i] == setsmap[j]:
                union(i, j)

    count = 0
    for i in range(n):
        if union_find[i] == i: count += 1

    print(count)


            
