def printL( P ) :
    print(''.join(P))
for testcases in range(int(input() ) ):
    pres = int(input())
    num, den = 103993, 33102
    ans = [ '3' ]
    if( pres == 0 ):
        printL(ans) 
    else :
        ans.append('.')
        num = (num % den) * 10
        for i in range( 1, pres+1 ) :
            quo, rem = divmod(num , den )
            ans.append(str(quo))
            num = rem * 10
        printL(ans)