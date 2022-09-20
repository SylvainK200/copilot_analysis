def lcollis():
    T = int(input())
    for t in range(T):
        N, M = list(map(int, input().split()))
        tmp = [0] * M
        for n in range(N):
            a = list(map(int, input()))
            for m in range(M):
                tmp[m] += a[m]
        res = 0
        for m in range(M):
            res += tmp[m] * (tmp[m]-1) / 2
        print(res)

if __name__ == '__main__':
    lcollis()
