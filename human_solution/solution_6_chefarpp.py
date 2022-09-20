##Codechef
##Chef and Subarrays
##2016.02.19

testCase = int(input())

for i in range(testCase):
    n = int(input())  # the number of elements
    array = list(map(int, input().strip().split()))
    count = 0 # the number of subarrays which satisfies specification
    start = 0


    for i in range(start, n):
        add = 0
        mul = 1

        while i < n:
            add += array[i]
            mul *= array[i]
            if add == mul:
                count +=1
            i+=1
        start += 1

    print(count)

        
            
