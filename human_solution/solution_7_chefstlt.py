T = eval(input())

for hell in range(T):
    first = list(input())
    second = list(input())

    ctr_max = 0
    ctr_min = 0

    for n,x in enumerate(first):
        if first[n] != '?'and second[n] != '?'and second[n] != first[n]:
                ctr_max += 1
                ctr_min += 1

        elif first[n] == '?'or second[n] == '?':
            ctr_max += 1

    print(ctr_min, ctr_max)
