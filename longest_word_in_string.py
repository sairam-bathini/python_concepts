given_string = "Cybersecurity is super cool and challenging"

new_list = given_string.split()
length_dict = {}

for i in new_list:
    length_dict[i] = len(i)

x = max(length_dict.values())

for i, j in length_dict.items():
    if j == x:
        print(i)         # Print the first longest word
        break            # Exit the loop after printing
