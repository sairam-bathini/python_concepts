# remove duplicate elements from the list and print a new list with unique elements

# i/p :[10,20,30,20,40,30]
# o/p: [10,20,30,40]

numbers = input().split(",")

list1 = [int(i) for i in numbers]
new_list = []

for i in list1:
    if i in new_list:
        continue
    else:
        new_list.append(i)

print(new_list)

# another method    
# unique_list = list(set(new_list))
# print(unique_list)
