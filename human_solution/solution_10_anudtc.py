t=int(input())
while t>0:
    n=int(input())
    s=''
    if 360%n==0:
        s+='y '
    else:
        s+='n '

    if n<=360:
        s+='y '
    else:
        s+='n '

    if n<=26:
        s+='y '
    else:
        s+='n '

    print(s)
    t=t-1
    
