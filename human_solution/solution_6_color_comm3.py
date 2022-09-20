def checker( pt1, pt2, R ) :
    dist2 = ( ( (pt1[0] - pt2[0]) **2 ) + ( (pt1[1] - pt2[1]) **2 ) )
    return True if (dist2 <= (R**2)) else False

for testcases in range(int(input() ) ) :
    maxD = int( input() )
    A = list(map(int, input().split() ))
    B = list(map(int, input().split() ))
    C = list(map(int, input().split() ))
    commList = [ checker(A, B, maxD), checker(B, C, maxD), checker(C, A, maxD) ]
    print('yes' if commList.count(True) > 1 else 'no')