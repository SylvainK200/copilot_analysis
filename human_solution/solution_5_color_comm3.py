t = int(input())
t1 = []
for q in range(t):
    x = int(input())
    a = []
    for i in range(3):
        a.append(list(map(int,input().split())))
    for i in range(3):
        z = 0
        for j in range(3):
            if j != i :
                if abs((((a[i][1]-a[j][1])**2)+((a[i][0]-a[j][0])**2))**0.5) > x :
                    for p in range(3):
                        if p != i and p!= j :
                            if abs((((a[i][1]-a[p][1])**2)+((a[i][0]-a[p][0])**2))**0.5)  <= x and abs((((a[j][1]-a[p][1])**2)+((a[j][0]-a[p][0])**2))**0.5) <= x  :
                                pass
                            else :
                                z = 1
    if z == 0:
        t1.append("yes")
    else :
        t1.append("no")
for i in range(len(t1)):
    print(t1[i])
            
        

    
    
    
