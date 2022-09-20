for _ in range(eval(input())):
    n=eval(input())
    if n>360:
        print('n n n')
    else:
        if 360%n==0:
            print('y', end=' ')
        else:
            print('n', end=' ')
        if n<=360:
            print('y', end=' ')
        else:
            print('n')
        if n*(n+1)/2<=360:
            print('y')
        else:
            print('n')
        
