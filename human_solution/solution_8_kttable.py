t = int(input())

for i in range(t):
    num = int(input())

    a = []
    b = []

    no = input().split()
    for n in no:
        a.append(int(n))

    no = input().split()

    for n in no:
        b.append(int(n))

    count = 0

    for i in range(num):
        if i == 0:
            if b[i] <= a[i]:
                count = count + 1
        else:
            if b[i] <= a[i] - a[i - 1]:
                count = count + 1

    print(count)
