transaction_amount,bank_balance = list(map(float,input().split()))
if transaction_amount<(bank_balance-0.5) and transaction_amount%5==0:
        print(('%.2f'%(bank_balance-transaction_amount-0.5)))
else:
    print(('%.2f'%bank_balance))