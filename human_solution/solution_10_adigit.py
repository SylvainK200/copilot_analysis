[n, m] = [int(x) for x in input().split(" ")]
a = input().rstrip()
digits = [int(x) for x in a]

L = len(a)
# construct
p = [[0]*L for _ in range(10)]
for i, x in enumerate(digits):
    p[x][i] = 1
for i in range(1, L):
    for j in range(10):
        p[j][i] += p[j][i-1]

for _ in range(m):
    t = int(input()) - 1
    # < digits[t]
    s_low = 0
    for i in range(digits[t]):
        s_low += p[i][t] * (digits[t] - i)
    s_high = 0
    for i in range(digits[t], 10):
        s_high += p[i][t] * (i - digits[t])
    print((s_low + s_high))
