N = list(input())
c = ch = che = chef = 0
for i in N:
    if i == 'C':
        c += 1
    elif i == 'H' and c > 0:
        c -= 1
        ch += 1
    elif i == 'E' and ch > 0:
        ch -= 1
        che += 1
    elif i == 'F' and che > 0:
        che -= 1
        chef += 1
print(chef)
