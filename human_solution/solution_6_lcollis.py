t = int(input())

for i in range(t):
    n, m = list(map(int, input().split()))
    arr = []
    for i in range(n):
        arr.append(input())
    
    coll = 0
    for i in range(m):
        x = 0
        for j in range(n):
            if arr[j][i] == '1':
                x += 1
        coll += x*(x-1)/2
    print(coll)
    