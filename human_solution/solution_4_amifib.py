def fib(x):
    a=0
    b=1
    if x==1:
        return a
    elif x==2:
        return b
    else:
        for x in range(x-2):
            c=a+b
            a=b
            b=c
        return c
t=int(input())
for x in range(t):
    n=int(input())
    i=0
    j=4790
    c="NO"
    for y in range(14):
        if j-1==2 and n!=fib((i+j)/2):
            break
        if n>fib((i+j)/2):
            i=(i+j)/2
        
        if n<fib((i+j)/2):
            j=(i+j)/2
        if n==fib((i+j)/2):
            c="YES"
            break
    print(c)        
        
