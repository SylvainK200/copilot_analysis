for _ in range(eval(input())):
        n = eval(input())
        if 360%n == 0:
                print('y', end=' ')
        else:
                print('n', end=' ')
        if n < 361:
                 print('y', end=' ')
        else:
                print('n', end=' ')
        if n*(n+1)/2 < 361:
                print('y')
        else:
                print('n')