# cook your code here
for _ in range(eval(input())):
    text1 = []
    text1 = list(map(int,input().split()))
    text2 = []
    text2 = list(map(str,input().split()))
    text3 = [] 
    for i in range(text1[1]):
        text3 += list(map(str,input().split()))
    ans = ""
    for i in text2:
        if i in text3:
            ans += "YES "
        else:
            ans += "NO "
    print(ans[0:-1])       