choices = ["addi", "subi", "muli", "divi"]

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter numerical values.")
        continue

    choose_operation = input("Enter your choice from (addi, subi, muli, divi): ")
    if choose_operation == "addi":
        print(f"The result of addition is {num1 + num2}")
    elif choose_operation == "subi":
        print(f"The result of subtraction is {num1 - num2}")
    elif choose_operation == "muli":
        print(f"The result of multiplication is {num1 * num2}")
    elif choose_operation == "divi":
        print(f"The result of division is {num1/ num2}")
    else:
        print("Please choose from the choices given (addi, subi, muli, divi)")
    
    choose_again = input("Would you like to perform more operations (yes/ quit): ")
    if choose_again != "yes":
        print("Thanks for using the calculator!")
        break
