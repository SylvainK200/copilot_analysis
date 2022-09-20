def intersection(set1,set2):
    ans = []
    for i in set1:
        if(i in set2):
            ans.append(i)
    return ans
def union(set1,set2):
    ans = set1[:]
    for i in set2:
        if(i not in set1):
            ans.append(i)
    return ans
def issubset(set1,set2):
    for i in set1:
        if(i not in set2):
            return False
    return True
def remove(set1,set2):
    for i in set2:
        set1.remove(i)
def atoms(sets,size,n,m):
    count = 0
    mainset = list(range(n))
    while(mainset != []):
        atom = []
        for i in mainset:
            valid = True
            for j in sets:
                if(issubset(atom+[i],j) or intersection(atom+[i],j) == []):
                    pass
                else:
                    valid = False
                    break
            if(valid):
                atom.append(i)
        count += 1
        remove(mainset,atom)
    return count
t = eval(input())
i = 0
while(i < t):
    n,m = [int(x) for x in input().split(" ")]
    sets = []
    size = []
    j = 0
    while(j < m):
        myset = [int(x) for x in input().split(" ")]
        size.append((int(myset[0])))
        sets.append(myset[1:])
        j += 1
    print(atoms(sets, size,n,m))
    i += 1