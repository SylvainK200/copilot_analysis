for i in range(int(input())):
    a=int(input())
    b=input()
    if b.count('Y')!=0:
        print("NOT INDIAN")
    elif b.count("I")!=0:
        print("INDIAN")
    else:
        print("NOT SURE")