def find_sub(set, n, target):
    if target == 0: return True
    if n == 0 and target > 0: return False
    if set[n-1] > target: return find_sub(set, n-1, target)
    if find_sub(set, n-1, target) or find_sub(set, n-1, target-set[n-1]): return True
    return False

def main():
    N_cases = int(input())
    for i in range(N_cases):
        n, m = [int(n_m) for n_m in input().split()]
        a = [int(input()) for x in range(n)]
        if find_sub(a, len(a), m): print("Yes")
        else: print("No")

if __name__ == "__main__":
    main()