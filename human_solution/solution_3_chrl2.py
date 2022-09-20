def process_problem_statement():
    A = list(input())
    
    count_dict = {'C': 0, 'H': 0 , 'E': 0, 'F': 0 }
    
    for x in range(0,len(A)):
        if A[x] == 'C':
            count_dict['C'] += 1
        elif A[x] == 'H':
            cC = count_dict['C']
            cH = count_dict['H']
            if cC > cH:
                count_dict['H'] = cH +1
        elif A[x] == 'E':
            cC = count_dict['H']
            cH = count_dict['E']
            if cC > cH:
                count_dict['E'] = cH +1
        elif A[x] == 'F':
            cC = count_dict['E']
            cH = count_dict['F']
            if cC > cH:
                count_dict['F'] = cH +1
            
    print(count_dict['F'])
    
process_problem_statement()