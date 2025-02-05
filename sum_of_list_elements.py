# sum of list elements

list = input().split(",")
new_list = []
sum = 0
for i in range(len(list)):
    new_list.append(int(list[i]))

for i in range(len(new_list)):
    sum = sum + new_list[i]

print(f"Sum of elements = {sum}")
