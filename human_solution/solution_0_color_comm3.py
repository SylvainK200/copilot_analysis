t=eval(input())
def dist(a,b,c,d):
    return (((a-c)**2)+((b-d)**2))**0.5
for i in range(0,t):
    r=eval(input())
    e=[]
    for j in range(0,3):
        e.append(list(map(int,input().split(' '))))
    if dist(e[0][0],e[0][1],e[2][0],e[2][1])<=r:
        print("yes")
    elif dist(e[0][0],e[0][1],e[1][0],e[1][1])<=r and dist(e[1][0],e[1][1],e[2][0],e[2][1])<=r:
        print("yes")
    else:
        print("no")