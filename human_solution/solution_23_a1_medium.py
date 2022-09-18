#!/usr/bin/python
import sys
def pns(seq):
    P, N = 0, 0
    for e in seq:
        if e >= 0:
            P += e
        else:
            N += e
    return P, N
def ss(seq, s=0):
    P, N = pns(seq)
    if not seq or s < N or s > P:
        return False
    n, m = len(seq), P - N + 1
    table = [[False] * m for x in range(n)]
    table[0][seq[0]] = True
    for i in range(1, n):
        for j in range(N, P+1):
            table[i][j] = seq[i] == j or table[i-1][j] or table[i-1][j-seq[i]]
    return table[n-1][s]
def vs(v):
    ta = []
    qn = v[0]
    v.pop(0)
    if qn > 20:
        raise Exception("Your wallet does not hold more than 20 banknotes!")
    qe = v[0]
    v.pop(0)
    
    for j in range(0,qn):
        if v[j] > 1000:
            raise Exception("The value of a single banknote is never more than 1000!")
        ta.append(v[j]);
    del v[0:qn]
    if ss(ta,qe):
        print("Yes")
    else:
        print("No")
    return v
#init----------------------------------------------------------------------------
v = []
#with open("./input.txt","r") as file:
for line in sys.stdin:
    if len(line) == 3:
        v.append(int(line))
    else:
        for x in line.split(' '):
            v.append( int(x.strip()) )
v.pop(0)
while len(v) > 2:
    v = vs(v)
#print v