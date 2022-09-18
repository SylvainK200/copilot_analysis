import sys
import math

M = 1000000007

rs = {}

def fn(An, En, V):
    global rs, M
    if V < 0:
        return 0

    try:
        return rs[An][En][V]
    except:
        if An in rs:
            if En not in rs[An]:
                rs[An][En] = {}
        else:
            rs[An] = {}
            rs[An][En] = {}

        rs[An][En][V] = None
        if V < An:
            rs[An][En][V] = 0
        else :
            if An ==0 or En == 0:
                if An == 0 and En == 0:
                    if V == 0:
                        rs[An][En][V] = 1
                    else:
                        rs[An][En][V] = 0
                else:                
                    if An == 1 and En == 0:
                        if V == 0:
                            rs[An][En][V] = 0
                        else:
                            rs[An][En][V] = 1
                    else:
                        if An == 0 and En == 1:
                            rs[An][En][V] = 1

        if rs[An][En][V] == None:
            vRemain = V - An
            s = (An + En) / 2
            cnt = 0
            for an1 in range(max(0, s - En), min(An, s)+1):
                cnt += fn(an1, s - an1, vRemain) * fn(An - an1, En - s + an1, vRemain)
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
