

def find_pairs(n, a):
    """
    >>> find_pairs(2, [2, 1])
    1
    >>> find_pairs(3, [3, 1, 2])
    3
    """
    a.sort()
    return sum(1 for i in range(n-1) for j in range(i+1, n) if a[i] < a[j])
for i in range (int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    print(find_pairs(n, l))