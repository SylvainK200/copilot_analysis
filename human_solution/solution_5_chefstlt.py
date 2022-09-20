
t = eval(input())
for i in range(t):
    s1 = input()
    s2 = input()
    min = 0
    max = 0
    for j,k in zip(s1,s2):
        if(j != '?' and k != '?'):
            if(j==k):
                min+=0
                max+=0
            else:
                min+=1
                max+=1
        elif(j == '?' and k != '?'):
            min+=0
            max+=1
        elif(j != '?' and k == '?'):
            min+=0
            max+=1
        elif(j == '?' and k == '?'):
            min+=0
            max+=1
    print(min,max)