for cas in range(eval(input())):
    n, c, Fc1, Fc2 = eval(input()), 1, 1, 2
    while Fc2 <= n:
        Fc1, Fc2, c = Fc2, Fc1+Fc2, c+1
    print(c)
