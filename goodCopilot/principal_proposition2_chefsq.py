T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    F = int(input())
    B = list(map(int, input().split()))
    if F > N:
        print("No")
    else:
        for i in range(N-F+1):
            if A[i:i+F] == B:
                print("Yes")
                break
        else:
            print("No")