import math
t = int(input())
for i in range(0,t):
    arr = []
    rem = [] 
    text = input()
    arr += text.split(" ")
    val1 = int(arr[0])
    val2 = int(arr[1])
    for j in range(1,val2+1):
        rem += [val1%j]
    print((max(rem)))    