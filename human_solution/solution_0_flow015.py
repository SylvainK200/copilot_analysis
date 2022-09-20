import datetime
n=int(input())
dic={0:'monday',1:'tuesday',2:'wednesday',3:'thursday',4:'friday',5:'saturday',6:'sunday'}
for i in range(n):
    yr=int(input())
    print(dic[datetime.date(yr,1,1).weekday()])