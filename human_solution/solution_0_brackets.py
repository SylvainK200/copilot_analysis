def F(s):
    balance = 0
    max_balance = 0
    for i in s:
        if i == '(':
            balance = balance + 1
        else:
            balance = balance - 1
        max_balance = max( max_balance, balance )
    return max_balance

n = eval(input())
for i in range(0,n):
    s = input()
    x = F(s)
    print('('*x+')'*x)
