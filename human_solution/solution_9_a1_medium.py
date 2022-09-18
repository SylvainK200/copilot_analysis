T = eval(input())
for _ in range(T):
        n,m = list(map(int, input().strip().split()))
        notes = [0]
        sum = []
        for _ in range(n):
                b = eval(input())
                for note in notes:
                        sum.append(note + b)
                sum.append(b)
                notes = set(sum[:])
        print('Yes' if m in notes else 'No')