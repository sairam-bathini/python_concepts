
# Here are simple examples for each string method:
==========================================================================================================================================================================
1. str.upper()
# Converts all characters in a string to uppercase.

text = "hello"
print(text.upper())  # Output: "HELLO"
==========================================================================================================================================================================
2. str.lower()
# Converts all characters in a string to lowercase.

text = "HELLO"
print(text.lower())  # Output: "hello"
==========================================================================================================================================================================
3. str.capitalize()
# Capitalizes the first character of the string.

text = "hello world"
print(text.capitalize())  # Output: "Hello world"
==========================================================================================================================================================================
4. str.title()
# Capitalizes the first letter of each word in the string.

text = "hello world"
print(text.title())  # Output: "Hello World"
==========================================================================================================================================================================
5. str.strip()
# Removes leading and trailing whitespace (spaces, newlines, tabs).

text = "  hello  "
print(text.strip())  # Output: "hello"
==========================================================================================================================================================================
6. str.lstrip()
# Removes leading whitespace from the string.

text = "  hello"
print(text.lstrip())  # Output: "hello"
==========================================================================================================================================================================
7. str.rstrip()
# Removes trailing whitespace from the string.

text = "hello  "
print(text.rstrip())  # Output: "hello"
==========================================================================================================================================================================
8. str.startswith(prefix)
# Checks if the string starts with a specified prefix.

text = "hello world"
print(text.startswith("hello"))  # Output: True
==========================================================================================================================================================================
9. str.endswith(suffix)
# Checks if the string ends with a specified suffix.

text = "hello world"
print(text.endswith("world"))  # Output: True
==========================================================================================================================================================================
10. str.replace(old, new)
# Replaces occurrences of a substring with another substring.

text = "hello world"
print(text.replace("world", "Python"))  # Output: "hello Python"
==========================================================================================================================================================================
11. str.split(separator)
# Splits the string into a list based on a separator.

text = "apple,banana,grape"
print(text.split(","))  # Output: ['apple', 'banana', 'grape']
==========================================================================================================================================================================
12. str.join(iterable)
# Joins elements of an iterable into a single string.

words = ["apple", "banana", "grape"]
print("-".join(words))  # Output: "apple-banana-grape"
==========================================================================================================================================================================
13. str.find(substring)
# Finds the first occurrence of a substring and returns the index, or -1 if not found.

text = "hello world"
print(text.find("world"))  # Output: 6
==========================================================================================================================================================================
14. str.rfind(substring)
# Finds the last occurrence of a substring and returns the index, or -1 if not found.

text = "hello world, welcome to the world"
print(text.rfind("world"))  # Output: 24
==========================================================================================================================================================================
15. str.index(substring)
# Finds the first occurrence of a substring and returns the index, raises an error if not found.

text = "hello world"
print(text.index("world"))  # Output: 6
==========================================================================================================================================================================
16. str.rindex(substring)
# Finds the last occurrence of a substring and returns the index, raises an error if not found.

text = "hello world, welcome to the world"
print(text.rindex("world"))  # Output: 24
==========================================================================================================================================================================
17. str.count(substring)
# Counts the occurrences of a substring in a string.

text = "hello world, welcome to the world"
print(text.count("world"))  # Output: 2
==========================================================================================================================================================================
18. str.isalnum()
# Checks if the string contains only alphanumeric characters (letters and numbers).

text = "Hello123"
print(text.isalnum())  # Output: True
==========================================================================================================================================================================
19. str.isalpha()
# Checks if the string contains only letters (no numbers or spaces).

text = "Hello"
print(text.isalpha())  # Output: True
==========================================================================================================================================================================
20. str.isdigit()
# Checks if the string contains only digits (0-9).

text = "12345"
print(text.isdigit())  # Output: True
==========================================================================================================================================================================
21. str.islower()
# Checks if all characters in the string are lowercase.

text = "hello"
print(text.islower())  # Output: True
==========================================================================================================================================================================
22. str.isupper()
# Checks if all characters in the string are uppercase.

text = "HELLO"
print(text.isupper())  # Output: True
==========================================================================================================================================================================
23. str.isspace()
# Checks if the string contains only whitespace characters.

text = "   "
print(text.isspace())  # Output: True
==========================================================================================================================================================================
24. str.isnumeric()
# Checks if the string contains only numeric characters.

text = "12345"
print(text.isnumeric())  # Output: True
==========================================================================================================================================================================
25. str.isdecimal()
# Checks if the string contains only decimal numbers.

text = "12345"
print(text.isdecimal())  # Output: True
==========================================================================================================================================================================
26. str.startswith(prefix, start, end)
# Checks if a substring in the specified range starts with the given prefix.

text = "hello world"
print(text.startswith("world", 6, 11))  # Output: True
==========================================================================================================================================================================
27. str.endswith(suffix, start, end)
# Checks if a substring in the specified range ends with the given suffix.

text = "hello world"
print(text.endswith("world", 6, 11))  # Output: True
==========================================================================================================================================================================
# These examples illustrate the most common string methods in Python with simple and clear outputs. 🚀
