
def main():

    w=(input())
    
    w=w.split(' ')
   
    b=float(w[1])
    w=int(w[0])
    if(w%5==0 and (w<b-0.50)):
        print(("%.2f" %(b-w-0.50)))
    else:
        print(("%.2f" %b))

main()        
    

