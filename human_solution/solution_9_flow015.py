import calendar
T=int(input())
week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']        
for t in range(T):
    inyear = int(input())
    c = calendar.weekday(inyear,1,1)
    print(week[c])