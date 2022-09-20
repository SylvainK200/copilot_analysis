#!/usr/bin/python

person=eval(input())
while person>0:
  s = input()
  numbers = list(map(int, s.split()))
  numbers.sort()
  print(numbers[1])
  person=person-1
#print "List : ", numbers
