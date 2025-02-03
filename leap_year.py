# Leap Year
# input: enter any year
# output: It is a leap year or It is not a Leap year

year = int(input())

if year%100 == 0 and year%400 != 0:
    print("It is not a Leap year")
elif year%4 == 0:
    print("It is a Leap year")
else:
    print("It is not a leap year")
