n=int(input())
import math


for _ in range(n):
    d=int(input())
    x=[int(i) for i in input().strip().split(' ')]
    y=[int(i) for i in input().strip().split(' ')]
    z=[int(i) for i in input().strip().split(' ')]
    a=math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)
    b=math.sqrt((x[0]-z[0])**2+(x[1]-z[1])**2)
    c=math.sqrt((z[0]-y[0])**2+(z[1]-y[1])**2)
    if (a<=d and b<=d) or (a<=d and c<=d) or (c<=d and b<=d):
        print('yes')
    else:
        print('no')
        

        
            
        
        
    
    

            
            
            
        
        
        
    
    
    
    

        
        


    
    
    
    
