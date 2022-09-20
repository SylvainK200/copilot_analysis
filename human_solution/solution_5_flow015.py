T=int(input())

WeekDays = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

years = list(range(1900,2501,1))
def isLeaps(years):
    f = lambda x:x%4==0 and (x%100 or x%400 ==0)
    return len(list(filter(f,years)))



for i in range(T):
    year = int(input())
    diff = year -2001

    if diff >= 0:
        leaps = isLeaps(list(range(2001,year,1)))
        print(WeekDays[(diff+leaps)%7  ])
    else:
        leaps = isLeaps(list(range(year,2001,1)))
        print(WeekDays[-(((-diff)+leaps)%7)])