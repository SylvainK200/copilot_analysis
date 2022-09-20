t=int(input())
while t:
    s = input()
    length = len(s)
    i=0
    maximum = 0
    count=0
    while i<length:
        while i<length and s[i]=='#':
            i+=1
        j=i
        while i<length and s[i]=='.':
            i+=1
        if i-j>maximum:
           count+=1
           maximum = i-j
    print(count)
    t-=1