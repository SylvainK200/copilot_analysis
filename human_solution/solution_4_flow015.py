from datetime import date
t=int(input())
for i in range(t):
    year=int(input())
    dayint=date(year, 1, 1).weekday()
    if(dayint==0):
        print("monday")
    elif(dayint==1):
        print("tuesday")
    elif(dayint==2):
        print("wednesday")
    elif(dayint==3):
        print("thursday")
    elif(dayint==4):
        print("friday")
    elif(dayint==5):
        print("saturday")
    elif(dayint==6):
        print("sunday")