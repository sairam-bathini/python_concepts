# list = list(map(int, input().split(",")))
# asteriod_sum = 9

new_list = []

def asteriods(list, asteriod_sum):
    length = len(list)

    for i in range(length-1):
        if list[i] + list[i+1] == asteriod_sum:
            new_list.append(list[i])
            new_list.append(list[i+1])
    print(new_list)

asteriods([2, 7, 11, 15], 9)
