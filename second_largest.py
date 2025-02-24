list_of_num = input().split(" ")
new_list = [int(i) for i in list_of_num]

def second_max(new_list):
    no_dup_list = list(set(new_list))
    no_dup_list.sort()
    print(no_dup_list)
    print(no_dup_list[-2])
    
second_max(new_list)
