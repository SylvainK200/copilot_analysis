def main():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        x = list(map(int, input().split()))
        mmin, mmax = n, -1
        mmin = min(x)
        mmax = max(x)
        ans = [0] * n
        for j in range(n):
            ans[j] = max(abs(mmin - j), abs(mmax - j))
        print(*ans)
main()