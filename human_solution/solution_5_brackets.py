tc = eval(input())
for i in range(tc):
    x= input()
    bal=0
    mbal=0
    for i in range(len(x)):
        if x[i]== '(':
            bal+=1
        if x[i]== ')':
            bal-=1
        mbal=max(mbal,bal)
    nl = []
    for i in range(mbal):nl.append('(')
    for i in range(mbal):nl.append(')')
    print(''.join(nl))

