string1 = input()

def reverse_string(string1):
    reverse_string = ""
    for ch in string1:
        reverse_string = ch + reverse_string
    
    print(reverse_string)

reverse_string(string1)
