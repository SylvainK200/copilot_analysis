test_cases = int(input())
while(test_cases > 0):
    test_cases -= 1
    n,k = list(map(int, input().split(' ')))
    max_profit = 0
    for i in range(1, k+1):
        if (n%i > max_profit): max_profit = n%i
    print(max_profit) 