
t=int(eval(input()))
while t>0:
    hd,cc,ts= list(map(float,input().split()))
    if hd>50 and cc<0.7 and ts>5600:
        print(10)
    elif hd>50 and cc<0.7:
        print(9)
    elif cc<0.7 and ts>5600:
        print(8)
    elif hd>50 and ts>5600:
        print(7)
    elif hd>50 or cc<0.7 or ts>5600:
        print(6)
    else:
        print(5)
    t=t-1
    