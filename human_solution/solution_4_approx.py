t=int(input())
while t:
    t=t-1
    a=103993
    b=33102
    a=a%b
    a=a*10
    s=""
    k=int(input())
    if k==0:
        s=s+"3"
    else:
        s=s+"3."
    for i in range(0,k):
        s=s+chr(a/b + 48)
        a=a%b
        a=a*10
    print(s)