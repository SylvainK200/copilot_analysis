# codeChef problem Code: ANUDTC
for testcases in range( int( input() ) ) :
    N = int(input() )
    print('y' if ( 360 % N == 0 ) else 'n', ' ', end=' ') 
    print('y' if ( N < 361 ) else 'n', ' ', end=' ')
    print('y' if ( ( (N * (N+1) ) / 2 ) < 361 ) else 'n')