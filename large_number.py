# Largest number
# input: 3 numbers
# output: The largest numnber is 

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 > num2 and num1 > num3:
    print(f"The largest number is:{num1}")
elif num2 > num1 and num2 > num3:
    print(f"The largest number is:{num2}")
else:
    print(f"The largest number is:{num3}")
