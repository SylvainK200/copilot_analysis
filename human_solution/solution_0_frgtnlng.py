t=eval(input())
while t:
    t=t-1
    a,b=list(map(int,input().split()))
    m=input()
    m=m.split(' ')
    n=''
    for i in range(0,b):
        d=input()
        n=n+d
        n=n+' '
    for i in range(0,a):
        if m[i] in n:
            print('YES', end=' ')
        else:
            print('NO', end=' ')
    print() 
        
