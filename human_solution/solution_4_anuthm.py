t=int(eval(input()))
while t>0 :
    x,y=[int(a) for a in input().split()]
    ans=float(x+y-1)
    print(("%.6f" %ans))
    t=t-1