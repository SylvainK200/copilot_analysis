t = int(input())
for i in range(t):
    n = int(input())
    seq = list(map(int, input().split()))
    f = int(input())
    f_seq = list(map(int, input().split()))
    if f in seq:
        print("Yes")
    else:
        print("No")