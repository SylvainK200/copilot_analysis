"""
In a company an emplopyee is paid as under:
If his basic salary is less than Rs. 1500, then HRA = 10% of base salary and DA = 90% of basic salary.  If his salary is either equal to or above Rs. 1500, then HRA = Rs. 500 and DA = 98% of basic salary. If the Employee's salary is input, write a program to find his gross salary.

†NOTE:‡ Gross Salary = Basic Salary+HRA+DA


Input

The first line contains an integer †T‡, total number of testcases. Then follow †T‡ lines, each line contains an integer †salary‡.


Output
Output the gross salary of the employee.

Constraints

1 †≤‡ †T‡ †≤‡ 1000
1 †≤‡ †salary‡ †≤‡ 100000


Example

†Input‡

3 
1203
10042
1312

†Output‡

2406
20383.2
2624
"""
T = int(input())
for i in range(T):
    salary = int(input())
    if salary < 1500:
        HRA = salary * 0.1
        DA = salary * 0.9
        gross_salary = salary + HRA + DA
        print(gross_salary)
    elif salary >= 1500:
        HRA = 500
        DA = salary * 0.98
        gross_salary = salary + HRA + DA
        print(gross_salary)
    else:
        print("Invalid Input")

