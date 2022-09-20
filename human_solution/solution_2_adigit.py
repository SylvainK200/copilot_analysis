n,m = list(map(int,input().split()))
arr = input()
my = [0]*10

ans = [ 0 for i in range(n)]

for i in range(n):
    x = ord(arr[i])-48
    y = 0
    for j in range(10):
        ans[i] +=abs(x-j)*my[j]
    my[x] +=1

for i in range(m):
    x = eval(input())-1
    print(ans[x])
    


