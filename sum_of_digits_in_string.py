given_string = "abc12def3gh45"

temp = ""
total = 0

for i in given_string:
    if i.isdigit():
        temp = temp + i
    else:
        if temp != "":
            total = total + int(temp)
            temp = ""

# For any number at the end of the string
if temp != "":
    total += int(temp)

print(total)
