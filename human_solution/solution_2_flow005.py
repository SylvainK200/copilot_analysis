def occurences(n):
    count = 0
    while n > 0:
        if n >= 100:
            count += 1
            n = n - 100
        elif n >= 50:
            count += 1
            n = n - 50
        elif n >= 10:   
            count += 1
            n = n - 10
        elif n >= 5:
            count += 1
            n = n - 5
        elif n >= 2:
            count += 1
            n = n - 2
        elif n >= 1:
            count += 1
            n = n - 1
        else:
            print ()
    return count 
def Main():      
    number = int(eval(input()))
    for i in range(number):
        x = eval(input())
        print((occurences(x)))
        
if __name__ == "__main__":
    Main();