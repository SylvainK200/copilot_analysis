def DevuAndGrapes():
    """ Devu and Grapes """
    
    t = int(input())
    for idx in range(t):
        
        # Import parameters
        n, k = list(map(int, input().split(" ")))
        input_lst = list(map(int, input().split(" ")))
        
        # Compute # of adding or removing
        numbers = 0
        for num in input_lst:
            remainder = num % k
            
            if num >= k:
                numbers = numbers + min(remainder, k - remainder)
            # when k > input
            else:
                numbers = numbers + (k - remainder)
                
        print(numbers)
        
DevuAndGrapes()