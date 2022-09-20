T = int(input())
for i in range(0, T):
    A,B,C = list(map(int,input().strip().split()))
    if A+B+C == 180:
        print("YES")
    else:
       print("NO")