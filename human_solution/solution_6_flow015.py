from datetime import date
L = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] 
for _ in range(int(input())):
    a = int(input())
    print(L[date(a, 0o1,0o1).weekday()]) 