list_given_string = input().split()
x = ""

for i in list_given_string:
    x = x + i[::-1] + " "

print(x.strip())
