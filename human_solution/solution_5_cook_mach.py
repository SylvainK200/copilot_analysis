pow2 = []
for i in range(25) :
    pow2.append(2**i) 

for testcases in range(int(input() ) ) :
    a, b = list(map(int, input().split() ))
    op = 0
    
    while True :
        if ( a == b ) :
            break
        elif ( a > b ) :
            op += 1 
            a = a // 2
        else : 
            op += 1
            if a in pow2 :
                a *= 2
            else :
                a = a // 2
    print(op)