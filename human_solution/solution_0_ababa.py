s2 = ['AA', 'BB']
s2a = ['A', 'B']
s3 = ['ABA', 'BAB', 'AAB', 'BBA', 'BAA', 'ABB']
s3a = ['A', 'B', 'A', 'B', 'A', 'B']
t = int(input())
for i in range(t):
    s = input().upper()
    if len(s) == 2:
        if s in s2:
            print(s2a[s2.index(s)])
        else:
            print(-1)
    elif len(s) == 3:
        if s in s3:
            print(s3a[s3.index(s)])
        else:
            print(-1)
    else:
        if s[0] == 'A':
            s = 'B' + s
        else:
            s = 'A' + s
        if s[len(s) - 1] == 'A':
            s = s + 'B'
        else:
            s = s + 'A'
        n = len(s)
        if 'ABBA' in s or 'BAAB' in s:
            index = s.find('ABBA')
            if index < 0:
                index = s.find('BAAB')
            if index == 0:
                print(s[1] + s[3 : n - 1])
            elif index == n - 4:
                print(s[1 : n - 2])
            else:
                print(s[1 : index + 2] + s[index + 3: n - 1])
        else:
            print(-1)