# Number of test cases
tests = input()
collisions = [0] * int(tests)
for t in range(0, int(tests)):
    # Test case t
    people = input()
    [boys,girls] = people.split(' ')
    # Creating the matrix
    matrix = [[0 for x in range(int(boys))] for y in range(int(girls))]
    for n in range(0,int(boys)):
        likes = input()
        for m in range(0, int(girls)):
            matrix[m][n] = int(likes[m])
    # Counting collisions
    coll = 0
    for m in range(0, len(matrix)):
        for x in range(matrix[m].count(1)-1, 0, -1):
            coll += x
    collisions[t]= coll
# Output
for c in collisions:
    print(c)
