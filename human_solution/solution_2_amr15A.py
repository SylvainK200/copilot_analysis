no_of_tests = int(input())

no_even = 0 
no_odd = 0 

weapon_list = list(map(int, input().split()))

for weapon_no in weapon_list:
    if weapon_no % 2 == 0:
        no_even += 1
    else:
        no_odd += 1

if no_even > no_odd:
    print("READY FOR BATTLE")
else:
    print("NOT READY")