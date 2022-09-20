from fractions import gcd
for _ in range(eval(input())):
    N = eval(input())
    A = []
    A = list(map(int,input().split()))
    B = []
    j = len(A)-1
    while j > 0:
        B = gcd(A[j],A[j-1])
        A = A[:j]
        A[j-1] = B 
        j -= 1
    print(A[0])