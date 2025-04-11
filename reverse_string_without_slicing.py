new_string = "Madam"
length = len(new_string)
reverse_string = ""

for i in range(1, length+1):
    m = new_string[-i]
    reverse_string += m

print(reverse_string)
