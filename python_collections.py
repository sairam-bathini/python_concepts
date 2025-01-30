# As our starting point, it's crucial to understand what Python collections are. They help us manage multiple values efficiently and are categorized into Lists, Tuples, Sets, and Dictionaries.

# We will focus mainly on Lists and Strings. A fun fact here is that Lists are mutable (we can change them after creation), while strings are immutable (unalterable post-creation). Let's see examples:

# Defining a list and a string
my_list = [1, 2, 3, 4]
my_string = 'hello'

# Now let's try to change the first element of both these collections
my_list[0] = 100
# Uncommenting the below line will throw an error
# my_string[0] = 'H'

print(my_list) # print the my_list elements
