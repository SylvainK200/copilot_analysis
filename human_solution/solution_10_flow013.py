import math
t = int(input())
for i in range(0,t):
    sums = 0
    arr = []
    text = input()
    arr += text.split(" ")
    sums = int(arr[0]) + int(arr[1]) + int(arr[2])
    if sums == 180 and "0" not in arr:
        print("YES")
    else:
        print("NO")
    