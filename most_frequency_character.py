given_string = list(input().lower())

dict_new = {}

for i in given_string:
    if i != " ":
        dict_new[i] = dict_new.get(i, 0) + 1

max_freq = max(dict_new.values())

for i, j in dict_new.items():
    if j == max_freq:
        print(i)
        break   # Optional: stop at first one if multiple tied
