for testcases in range(int(input() ) ) :
    Str = input()
    day = 0
    jump = 1
    i = 0
    while ( i < len(Str) ):
        if (Str[i] == '#' ):
            i += 1
            continue
        else : 
            count = 1
            while ( Str[i] != '#' ):
                i += 1
                count += 1
            if count > jump :
                day += 1
                jump = count
    print(day)