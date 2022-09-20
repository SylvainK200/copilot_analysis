# breaking into atoms - atoms.py

t = int(input())

for iter in range(t):
    n,m = list(map(int, input().strip().split()))
    x = set(range(n))
    s = []
    for i in range(m):
        line = list(map(int, input().strip().split()))
        s.append( set(line[1:]) )

    masks = []
    for i in range(n):
        mask = 0
        for j in range(m):
            if i in s[j]:
                mask |= 1<<j
        masks.append(mask)

    sm = set(masks)
    print(len(sm))
        


        
    
    
