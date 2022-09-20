b=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
for i in range(int(input())):
    a=int(input())
    c=0
    for j in range(min(2001,a),max(2001,a),1):
        c+=365
        if (j%100!=0 and j%4==0) or (j%400==0):
            c+=1
    if a>=2001:
        print(b[c%7])
    else:
        print(b[-c%7])