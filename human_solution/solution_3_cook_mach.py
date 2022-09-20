from math import log

def cook(a, b):
    n = 0
    while int(log(a, 2)) != log(a, 2):
        a //= 2
        n += 1
    n += abs(int(log(b, 2) - log(a, 2)))
    return n

for i in range(int(eval(input()))):
    settings = input().split()
    a, b = int(settings[0]), int(settings[1])
    print((cook(a, b)))
