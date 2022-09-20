T=int(input())
for i in range(T):

    q=list(map(int,input().split()))
    q.sort()
    print(q.pop(1))
