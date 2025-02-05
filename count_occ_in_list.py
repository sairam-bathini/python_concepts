# count the number of occurences of a specific element in a list

# input [1,2,3,2,1,4,2,5]
#        2
# o/p count of 2 = 3

num = input().split(",")

my_list = [int(i) for i in num]

find_count_of = int(input())

count = 0

for i in my_list:
    if i == find_count_of:
        count +=1

print(f"Count of {find_count_of} = {count}")

# other solution
# count = my_list.count(2)
# print(count)
