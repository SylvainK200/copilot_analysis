def chefANDcoloring():
    for i in range(int(input())):
        n=int(input())
        inp=input()
        red=0
        blue=0
        green=0
        for j in inp:
            if(j=='R'):
                red=red+1
            elif(j=='B'):
                blue=blue+1
            else:
                green=green+1
        highest=max(red,blue,green)
        print(n-highest)
chefANDcoloring()
            
