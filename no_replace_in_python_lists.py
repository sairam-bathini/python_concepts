# In Python, lists don't have a replace function. Instead, you can directly assign a new value to a specific index in the list.

# For example, to replace the second element (index 1) with 100, you would use:

def modify_list(my_list):
  # Replace the second element (index 1) with '100'
  my_list[1] = 100
  
  # Append '200' to the end of the list
  my_list.append(200)
  # Print the modified list
  print(my_list)

# Example list
example_list = [10, 20, 30, 40 ,50]
modify_list(example_list)

