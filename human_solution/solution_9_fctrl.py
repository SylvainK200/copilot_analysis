T=int(input())
while T>0:
    T-=1
    N=int(input())
    p5=0
    p2=0
    n=0
    while N/pow(5,n):
        p5=N/pow(5,n)+p5
        n+=1
    p5-=N
    n=0
    while N/pow(2,n):
        p2=N/pow(2,n)+p2
        n+=1
    p2-=N
    if p2<p5:
        print(p2)
    else:
        print(p5)