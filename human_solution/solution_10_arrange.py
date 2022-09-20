def scramble(k, s):
    X = list(zip(s, list(range(2**k))))
    X = [[bin(x[1])[2:].rjust(k, '0'), x[0]] for x in X]
    X = [[int(''.join(reversed(x[0])), 2), x[1]] for x in X]
    X.sort()
    return ''.join([x[1] for x in X])

t = int(input())
for i in range(t):
    x = input().split()
    k, s = int(x[0]), str(x[1])
    print(scramble(k, s))
