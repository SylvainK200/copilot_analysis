t = int(input())
for i in range(t):
    line =input()
    jumps = 0
    max_jump = 0
    res = 0
    for c in line:
        if c == '#':
            if jumps > max_jump:
                res += 1
                max_jump = jumps
            jumps = 0
        else:
            jumps += 1
    print(res)