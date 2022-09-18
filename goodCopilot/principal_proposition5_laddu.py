def main():
    t = int(input())
    for i in range(t):
        n, origin = input().split()
        n = int(n)
        laddus = 0
        for j in range(n):
            activity = input()
            if activity == "CONTEST_WON":
                rank = int(input())
                if origin == "INDIAN":
                    laddus += 300 + 20 - rank
                else:
                    laddus += 300
            elif activity == "TOP_CONTRIBUTOR":
                laddus += 300
            elif activity == "BUG_FOUND":
                severity = int(input())
                if origin == "INDIAN":
                    laddus += 50 - severity
                else:
                    laddus += 50
            elif activity == "CONTEST_HOSTED":
                laddus += 50
        if origin == "INDIAN":
            print(int(laddus / 200))
        else:
            print(int(laddus / 400))
main()