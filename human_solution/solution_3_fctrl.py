noOfInputs = int(input())
for x in range(noOfInputs):
    varInput = int(input())
    flag = 0
    while varInput:
        varInput /= 5
        flag += varInput
    print(flag)
