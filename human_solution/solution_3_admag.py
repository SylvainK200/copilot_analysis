known=dict()
known = {0:0, 1:1}
def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res
t=int(input())
Fib=dict()
for i in range(2,90):
    Fib[i-1]=fibonacci(i)
while t>0:
    t=t-1
    ans=0
    n=int(input())
    for key,val in list(Fib.items()):
        if val>n:
            ans=key-1
            break
    print(ans)
