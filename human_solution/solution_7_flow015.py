from datetime import date as d
def leap(y):
    if y%400==0:
        return True
    elif y%100==0:
        return False
    elif y%4==0:
        return True
    else:
        return False
d={0:'monday',1:'tuesday',2:'wednesday',3:'thursday',4:'friday',5:'saturday',6:'sunday'}
for t in range(int(input())):
    x=0 
    y=int(input())
    if y>2001:
        for i in range(2001,y):
            if leap(i):
                x+=2
            else:
                x+=1
            x%=7
    else:
        for i in range(y,2001):
            if leap(i):
                x-=2
            else:
                x-=1
            x%=7
    print(d[x])
