n = int(input())
a = list(map(int,input().split()))
c_e = 0
for i in range(n) :
    if a[i] %2 == 0 :
        c_e += 1
if 2*c_e > n :
    print('READY FOR BATTLE')
else :
    print('NOT READY')
