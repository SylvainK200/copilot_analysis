w, b = list(map(float, input().split()))

if b < w + 0.5:
    print(b)
elif w%5 == 0:
    print("{0:.2f}".format(b - w - 0.50))
else:
    print(b)