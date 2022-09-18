"""
Write a program that takes in a letterclass ID of a ship and display the equivalent string class description of the given ID. Use the table below.

Class ID 
Ship Class

B or b
BattleShip


C or c
Cruiser


D or d
Destroyer


F or f
Frigate



Input

The first line contains an integer †T‡, total number of testcases. Then follow †T‡ lines, each line contains a character.


Output
Display the Ship Class depending on ID.

Constraints

1 †≤‡ †T‡ †≤‡ 1000


Example

†Input‡

3 
B
c
D

†Output‡
BattleShip
Cruiser
Destroyer
"""
test_cases = int(input())
for i in range(test_cases):
    ship_class = input()
    if ship_class == 'B' or ship_class == 'b':
        print('BattleShip')
    elif ship_class == 'C' or ship_class == 'c':
        print('Cruiser')
    elif ship_class == 'D' or ship_class == 'd':
        print('Destroyer')
    elif ship_class == 'F' or ship_class == 'f':
        print('Frigate')
    else:
        print('Invalid')
