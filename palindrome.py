# palindrome
# input: radar
# output: It is a palindrome or It is not a palindrome

take_input = input()
reverse_of_input = take_input[::-1]
if take_input == reverse_of_input:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
