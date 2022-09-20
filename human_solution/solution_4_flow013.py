t = eval(input())
for i in range(t):
    a1,a2,a3 = list(map(int,input().split(' ')))
    if(a1>=1 and a2>=1 and a3>=1 and a1+a2+a3 ==180):
        print("YES")
    else:
        print("NO")