n,m = list(map(int,input().split()))
arr = input()
array = [0]*n
mydict = {i:0 for i in range(10)}

for i in range(n):
    temp = ord(arr[i])-48
    for j in range(10):
        if temp>j:
            array[i] = (temp-j)*mydict[j]+array[i]
        else:
            array[i] = (j-temp)*mydict[j]+array[i]
    mydict[temp]+=1
    

for i in range(m):
    x = eval(input())
    print(array[x-1])



