T = int(input())

for t in range(T):
    N, K = input().split(' ')
    N, K = int(N), int(K)
    forgotten = input().split(' ')
    existing = set()
    for k in range(K):
        existing |= set(input().split(' ')[1:])
    print(' '.join(["YES" if word in existing else "NO" for word in forgotten]))
