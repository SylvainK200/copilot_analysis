t=int(input())
while t > 0 :
    t-=1
    x = input().strip()
    max_balance = balance = 0
    for i in range(len(x)) :
        if x[i] == '(' :
            balance += 1
        elif x[i] == ')' :
            balance -= 1
        max_balance = max(max_balance,balance)
    s = '('*max_balance + ')'*max_balance
    print(s)
    
