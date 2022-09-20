t = input().strip()
t = int(t)
for i in range(t):
    result=[]
    n,k = input().strip().split(" ")
    n = int(n)
    k = int(k)
    wlist = input().strip().split(" ")
    modern_words = []
    for j in range(k):
        modern_words += input().strip().split(" ")[1:]
    for j in range(n):
        if wlist[j] in modern_words:
            result.append("YES")
        else:
            result.append("NO")
    print(" ".join(result))