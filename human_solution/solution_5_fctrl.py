def recursionfac(x):
    if(x == 0):
        return 0
    return (x/5)+recursionfac(x/5)
i = eval(input())
counter = 0
while(counter < i):
    N = eval(input())
    print(recursionfac(N))
    counter += 1  