t = int(input())
for i in range(t):
    amount = int(input())
    n=0
    while amount>=100:
        amount-=100
        n+=1
    while amount>=50:
        amount-= 50
        n+=1
    while amount>=10:
        amount -= 10
        n+=1
    while amount>=5:
        amount-= 5
        n+=1
    while amount>=2:
        amount-= 2
        n+=1
    while amount>=1:
        amount-= 1
        n+=1
    print(n)
