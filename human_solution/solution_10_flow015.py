
from http.client import SWITCHING_PROTOCOLS

t = eval(input())
for i in range(t):
    n = eval(input())
    no_of_days = 0
    m = 2001
    while(n<m):
        m -=1
        if((m%4 == 0 and m%100!=0)or m%400 == 0):
            no_of_days -= 366
        else:
            no_of_days -= 365
    while(n>m):
        if((m%4 == 0 and m%100!=0)or m%400 == 0):
            no_of_days +=366
        else:
            no_of_days += 365
        m +=1
    day = no_of_days%7
    if(day == 0):
        print("monday")
    elif(day == 1):
        print("tuesday")
    elif(day == 2):
        print("wednesday")
    elif(day == 3):
        print("thursday")
    elif(day == 4):
        print("friday")
    elif(day == 5):
        print("saturday")
    elif(day == 6):
        print("sunday")