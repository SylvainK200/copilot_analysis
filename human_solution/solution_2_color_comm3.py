T = int(input())
for t  in range (T):
    R = int(input())**2
    a,b = list(map(int,input().split()))
    c,d = list(map(int,input().split()))
    x,y = list(map(int,input().split()))
    d1 = (a-c)**2 + (b-d)**2
    d2 = (c-x)**2 + (d-y)**2
    d3 = (a-x)**2 + (b-y)**2
    if d1<=R:
        if d2<=R:
            print("yes")
        elif d3<=R:
            print("yes")
        else:
            print("no")
    elif d2<=R:
        if d3<=R:
            print("yes")
        else:
            print("no")
    else:
        print("no")
