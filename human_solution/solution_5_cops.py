for i in range(eval(input())):
    MXY = list(map(int, input().split()))
    houseNos = list(map(int, input().split()))
    houseCover = MXY[1] * MXY[2]
    houseCoveredList = []
    for j in houseNos:
        if j - houseCover <= 0: houseCoveredList.extend(list(range(1, j + 1)))
        else: houseCoveredList.extend(list(range(j - houseCover, j + 1)))
        
        if j + houseCover > 100: houseCoveredList.extend(list(range(j, 101)))
        else: houseCoveredList.extend(list(range(j, j + houseCover + 1)))
    print(100 - len(set(houseCoveredList)))