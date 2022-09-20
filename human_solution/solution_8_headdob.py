# cook your code here
t = int(input())
for i in range(0,t):
    n = int(input())
    code = input();
    if "I" in code:
        print("INDIAN")
    elif "Y" in code:
        print("NOT INDIAN")
    else:
        print("NOT SURE")