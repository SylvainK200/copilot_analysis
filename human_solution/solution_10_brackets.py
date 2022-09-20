t = int(input())
for i in range(t):
    b = str(input())
    bal = malbal = 0
    for j in b:
        if j == '(':
            bal += 1
        else:
            bal -= 1
        malbal = max(malbal,bal)
    a = "("*malbal + ")"*malbal
    print(a)