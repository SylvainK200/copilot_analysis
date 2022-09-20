t= int(input())

for te in range(t):
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    count = 0
    for x in range(N):
        
        if x == 0:
            if A[x] >= B[x]:
               count += 1
               
        else:
            if (A[x] - A[x-1]) >= B[x]:
                count +=  1
                
    print(count)
