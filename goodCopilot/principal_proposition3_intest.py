def main():
    n, k = map(int, input().split())
    s = 0
    for i in range(n):
        x = int(input())
        if x % k == 0:
            s += 1
    print(s)
    
main()