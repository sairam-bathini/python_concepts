arr = [1,2,3,4,5]
reverse_arr = []

for i in range(1, len(arr)+1):
    reverse_arr.append(arr[-i])  

print(reverse_arr)
