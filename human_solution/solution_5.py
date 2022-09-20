# CodeChef
# Practice
# Easy
# Breaking Into Atoms

ntc = int(input())

for cti in range(ntc):
    ec, sc = list(map(int, input().split()))
    el = [0] * ec

    for si in range(sc):
        sb = 1 << si
        sl = list(map(int, input().split()[1:]))

        for se in sl:
            el[se] |= sb

    print(len(set(el)))
