def value(a,n) :
    if n not in l :
        if n == 0 :
            return a
        for i in range(len(l)-1) :
            if n < l[i+1] and n > l[i] :
                a += n / l[i]
                n = n % l[i]
        return value(a,n)
    else :
         return a+1
t = int(input().strip())
l = [1,2,5,10,50,100]
for i in range(t) :
    n = int(input().strip())
    if n > 100 :
        print(value(n/100,n%100))
    else :
        print(value(0,n))
