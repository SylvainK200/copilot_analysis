for i in range(int(input())):
    t = [i for i in map(int,input().split()) if i>0]
    print("YES" if sum(t)==180 and len(t) ==3 else "NO")
