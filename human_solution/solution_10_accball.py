t = int(input())
while t > 0:
    x = input()
    y = input()
    z = []
    for i in range(len(x)):
        if x[i] == y[i]:
            if x[i] == 'B' :
                z.append('W')
            else :
                z.append('B')
        else:
            z.append('B')
    print(''.join(map(str,z)))
    t = t-1 