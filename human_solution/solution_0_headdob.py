t = eval(input())
for n in range(0,t):
    test = eval(input())
    result = input()
    output = "NOT SURE"
    for t in range(0,test):
        if result[t] == "Y":
            output = "NOT INDIAN"
        elif result[t] == "I":
            output = "INDIAN"
        
    print(output)
    
