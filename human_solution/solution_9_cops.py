testcases = int(input())

def methodarearemaining(array, jump, totalarea):
    array.sort()
    remainingarea = 0
    for j in range(0,len(array)-1):
        if ((array[j+1]-array[j]) > (2*jump + 1)):
            remainingarea = remainingarea + ((array[j+1]-array[j]) - (2*jump + 1))
    if (array[0] > jump+1):
        remainingarea = remainingarea + (array[0] - (jump + 1))
    if (array[-1] < (totalarea - jump)):
        remainingarea = remainingarea + ((totalarea - jump) - array[-1])
    return remainingarea
        
for i in range(0, testcases):
    inputstring1 = [int(x) for x in input().split()]
    areajump = inputstring1[1] * inputstring1[2]
    copsresidence = [int] * inputstring1[0]
    copsresidence = [int(x) for x in input().split()]
    #print areajump
    #print copsresidence
    arearemaining = methodarearemaining(copsresidence, areajump, 100)
    print(arearemaining)