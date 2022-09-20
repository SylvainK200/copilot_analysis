#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# pylint: disable=C0111

'''input
10 3
0324152397
1
4
7
'''


def main():
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().strip()))
    occ = [[0]*10]
    occ[0][arr[0]] += 1

    for x in range(1, n):
        occ.append(occ[-1][:])
        occ[x][arr[x]] += 1

    for _ in range(m):
        q = int(input()) - 1
        s = 0

        for i, x in enumerate(occ[q]):
            s += abs(x * (i - arr[q]))

        print(s)


main()
