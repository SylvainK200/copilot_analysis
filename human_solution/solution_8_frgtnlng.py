cases = int(input())
temp = []

for i in range(0,cases):
    flag = 0
    temp = list(map(int,input().split(' ')))
    words = input().split(' ')
    phrases = []
    for j in range(0,temp[1]):
        tmp = input().split(' ')
        p_words = int(tmp[0])
        tmp.remove(tmp[0])
        phrases.append(tmp)
    #print words, phrases
    st = "" 
    for ele in words:
        for k in phrases:
            if ele in k:
                flag = flag+1
        if(flag == 0):
            print("NO", end=' ')
        else:
            print("YES", end=' ')
        flag=0
    print("\n", end=' ')
    

