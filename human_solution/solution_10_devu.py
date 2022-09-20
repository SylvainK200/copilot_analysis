def test2():
    matches = eval(input())
    result = []
    for _ in range(matches):
        first = input().split()
        tmp = input().split()
        buckets = []
        grapes_in_bucket = int(first[1])
        for index in range(int(first[0])):
            buckets.append(int(tmp[index]))

        count = 0
        for grapes in buckets:
            if grapes%grapes_in_bucket == 0:
                continue

            if grapes/grapes_in_bucket == 0:
                count += grapes_in_bucket - grapes
                continue
            
            min_grapes = abs(grapes - (grapes/grapes_in_bucket)*grapes_in_bucket)
            max_grapes = abs(grapes - (grapes/grapes_in_bucket + 1)*grapes_in_bucket)
            
            
            if min_grapes > max_grapes:
                count += max_grapes
            else:
                count += min_grapes
                
        result.append(count)    


    for e in result:
        print(e)

test2()
         