from collections import Counter
minr = 1
maxr = 10 ** 9 + 1
t = int(input())
for i in range(t):
    k = int(input())
    cnt = Counter()
    for j in range(k):
        op, num, ans = input().split()
        ans = ans.upper()
        num = int(num)
        if op == '<':
            if ans == 'YES':
                cnt[minr] += 1
                cnt[num] -= 1
            else:
                cnt[num] += 1
                cnt[maxr] -= 1
        elif op == '>':
            if ans == 'YES':
                cnt[num + 1] += 1
                cnt[maxr] -= 1
            if ans == 'NO':
                cnt[minr] += 1
                cnt[num + 1] -= 1
        else:
            if ans == 'YES':
                cnt[num] += 1
                cnt[num + 1] -= 1
            else:
                cnt[minr] += 1
                cnt[num] -= 1
                cnt[num + 1] += 1
                cnt[maxr] -= 1
    maxv = 0
    count = 0
    ind = sorted(cnt)
    for j in range(len(ind)):
        count += cnt[ind[j]]
        if maxv < count:
            maxv = count
    print(k - maxv)
    