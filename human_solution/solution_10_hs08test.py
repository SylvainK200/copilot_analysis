import sys
transaction = sys.stdin.readline().split()
amount = int(transaction[0])
balance = float(transaction[1])
bank_charge = 0.50
if amount%5 == 0:
    if balance - amount - bank_charge >= 0 :
    	new_balance = balance - amount - bank_charge
        print("%.2f" % new_balance)
    else:
        print(balance)
else:
    print(balance) 