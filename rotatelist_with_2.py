list_of_num = list(map(int, input().split()))
k = int(input())
new_list = []
another_list = []
for i in range(len(list_of_num)):
    if i >= k:
        new_list.append(list_of_num[i])
    else:
        another_list.append(list_of_num[i])

latest_list = new_list + another_list
print(latest_list)
