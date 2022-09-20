## Codechef
## Cooking Machine (Beginner)
## 2016.02.24. Wed

testCases = int(input())

for i in range(testCases):
    inputNum = list(map(int, input().strip().split()))
    ini = inputNum[0]  # the initial
    desiredVal = inputNum[1]  # the desired values
    count = 0

    if ini == desiredVal:
        print(count)

    else:
        if (ini & (ini-1)) == 0 and ini < desiredVal:
            while ini != desiredVal:
                ini *= 2
                count += 1
            print(count)

        elif (ini & (ini-1)) == 0 and ini > desiredVal:
            while ini != desiredVal:
                ini /= 2
                count += 1
                
            print(count)

        elif (ini & (ini-1)) != 0:
            while (ini & (ini-1)) != 0:
                ini /= 2
                count += 1

            if ini < desiredVal:
                while ini != desiredVal:
                    ini *= 2
                    count += 1
                print(count)

            elif ini == desiredVal:
                print(count)

            else:
                while ini != desiredVal:
                    ini /= 2
                    count += 1
                print(count)
            


