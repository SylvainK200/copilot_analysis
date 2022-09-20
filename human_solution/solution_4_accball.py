for _ in range(eval(input())):
    x = input()
    y = input()
    z = ''
    for i,j in zip(x,y):
        if i == 'B' and j == 'B' :
            z = z + 'W'
        else:
            z = z + 'B'
    print(z)
   