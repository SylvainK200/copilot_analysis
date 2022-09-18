import sys
import math

M = 1000000007

rs = {}

def fn(An, En, V, l=0):
    global rs, M
    if V < 0:
        return 0
    
    if An in rs:
        if En in rs[An]:
            if V in rs[An][En]:
                return rs[An][En][V]
        else:
            rs[An][En] = {}
    else:
        rs[An] = {}
        rs[An][En] = {}

    rs[An][En][V] = None
    if V < An:
        rs[An][En][V] = 0

    if An == 0 and En == 0:
        if V == 0:
            rs[An][En][V] = 1
        else:
            rs[An][En][V] = 0
    
    if An == 1 and En == 0:
        if V == 0:
            rs[An][En][V] = 0
        else:
            rs[An][En][V] = 1

    if An == 0 and En == 1:
        rs[An][En][V] = 1

    if rs[An][En][V] == None:
        vRemain = V - An
        s = (An + En) / 2
        cnt = 0
        for an1 in range(max(0, s - En), min(An, s)+1):
            an2 = An - an1
            en1 = s - an1
            en2 = En - en1
            cnt1 = cnt2 = 0
            cnt1 = fn(an1, en1, vRemain, l+1)
            cnt2 = fn(an2, en2, vRemain, l+1)
            cnt += cnt1 * cnt2
        rs[An][En][V] = cnt % M
    return rs[An][En][V]
    
def main():        
    testCases = int(sys.stdin.readline())
    cases = []
    for n in range(0, testCases):
        An, En, V = sys.stdin.readline().split(' ')
        print("%s" % ((fn(int(An), int(En), int(V)) - fn(int(An), int(En), int(V)-1) + M ) % M))
 
if __name__ == '__main__':
    main()
