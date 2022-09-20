t = eval(input())
for _ in range(t):
    s = input()
    a = []
    m = 0
    for i in s:
        
        if i == '.':
            m += 1
        else:
            if m != 0:
                a.append(m)
            m = 0

    
    day = 0
    temp = 0
    for i in range(len(a)):
        if temp < a[i]:
            temp = a[i]
            day += 1
    print(day)
