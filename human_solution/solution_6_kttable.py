for _ in range(eval(input())):
    n = eval(input())
    time_given = list(map(int, input().split()))
    time_required = list(map(int, input().split()))
    slots = [0] * len(time_given)
    slots[0] = time_given[0]
    for i in range(1, len(time_given)):
        slots[i] = time_given[i] - time_given[i - 1]

    count = 0
    for i in range(len(time_required)):
        if time_required[i] <= slots[i]:
            count += 1

    print(count)