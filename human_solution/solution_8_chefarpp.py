# cook your code here
def pro(arr):
    product = 1
    for i in arr:
        product = product * i
    return product
for _ in range(eval(input())):
    n = eval(input())
    a = []
    a = list(map(int,input().split()))
    sub = []
    j = 1
    while True:
        for i in range(n-j+1):
            sub.append(a[i:i+j])
        if j==len(a):
            break
        j +=1 
    count = 0    
    for i in sub:
        if sum(i) == pro(i):
            count += 1
    print(count)        