# find the max and min values in list of numbers

# input list of numbers 15, 2, 7, 25, 10
# output: Max = 25
#         Min = 2

list = input().split(",")
new_list = []
for i in range(len(list)):
    new_list.append(int(list[i]))

new_list.sort()
print(f"Max = {new_list[-1]}\nMin = {new_list[0]}")
