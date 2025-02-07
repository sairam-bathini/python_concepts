'''
To pack wisely, checking your packing list is essential. Can you add the code to check whether an item is on your packing list and determine its position?
Hint: Use list and string search functions to tackle this task. Which ones? Ask me if you don't remember!
'''
# Travel Packing List and Selection
packing_list = ['clothes', 'toothbrush', 'passport', 'camera']
item_to_check = 'passport'
is_item_packed = False
item_index = -1

# TODO: Write a line of code to check if the item_to_check is in the packing_list
for i in packing_list:
    if i == item_to_check:
        is_item_packed = True
        item_index = packing_list.index(i)
        print("Is the item packed?", is_item_packed)
        print("Item index:", item_index)
    else:
        continue


# TODO: Find the index of item_to_check in the list if it is packed, otherwise set it to -1

# Print out the results
