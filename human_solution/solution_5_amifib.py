import math
n=int(input())
arr=[1,2]
for i in range(2,5000):
    arr.append(arr[i-1]+arr[i-2])
#print arr
while n>0:
    a=int(input())
    if a in arr:
        print("YES")
    else:
        print("NO")
    n-=1