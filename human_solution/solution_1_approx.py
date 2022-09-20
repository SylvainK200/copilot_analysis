places = []
r = 103993
q = r
for _ in range(1000000):
    once = True
    while r < 33102:
        r *= 10
        if not once:
            places.append(0)
        once = False

    q, r = divmod(r, 33102)
    places.append(q)

cases = int(input())

for _ in range(cases):
    K = int(input())
    p = "." + "".join(map(str, places[1:K+1]))
    t = "3"
    if K:
        print(t + p)
    else:
        print(t)



