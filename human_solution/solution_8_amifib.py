
for cases in range(int(input())):
    n = int(input())
    if n == 0 or n == 1:
        print("YES")
        continue
    prev = 0
    curr = 1
    while curr < n:
        temp = curr + prev
        prev = curr
        curr = temp
    if curr == n:   print("YES")
    else:   print("NO")
        
    
