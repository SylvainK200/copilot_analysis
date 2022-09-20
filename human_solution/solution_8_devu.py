for _ in range(eval(input())):
    n,k = list(map(int,input().split()))
    grps = list(map(int,input().split()))
    cnt = 0
    for i in grps:
        rem = i % k
        if rem == 0:
            continue
        else:
            if i >= k:
                cnt += min(rem,k-rem)
            else:
                cnt += k - rem
    print(cnt)        