def main():
    n = int(input())
    for i in range(n):
        s = input()
        if len(s) == 1:
            print("YES")
            continue
        count = 0
        for c in s:
            if c == s[0]:
                count += 1
            else:
                count -= 1
        if count == 0:
            print("YES")
        else:
            print("NO")
main()