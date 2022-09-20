# python3

if __name__ == "__main__":

    l = []
    f = []
    x = int(input())
    while(x):
        l = (list(map(int,input().split())))
        l.sort()
        f.append(l[1])
        x = x - 1
    for i in f:
        print(i)
