t = eval(input())
while t:
    length = eval(input())
    init = 0
    count = 0
    list1 = list(map(int,input().split()))
    list2 = list(map(int,input().split()))
    for i in range(0,length):
        if ((list1[i]-init)>=list2[i]):
            count+=1
        init = list1[i]
    print(count)
    t-=1
