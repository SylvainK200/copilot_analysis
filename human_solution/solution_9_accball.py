t = int(input())

while t > 0:
    x = input()
    y = input()
    z = ''
    for i in range(len(x)):
        if x[i] == y[i] == 'B':
            z += 'W'
        elif x[i] == y[i] == 'W':
            z += 'B'
        else:
            z += 'B'
    print(z)
    t -= 1
