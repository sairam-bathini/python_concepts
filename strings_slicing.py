'''
Strings

String>> collection of characters or sequence of characters

Python uses zero-based indexing, where the first indexing starts from 0
Python also have negative-based indexing 

str =   H     E      L      L    O
         [0]   [1]   [2]    [3]   [4]
		 [-5]  [-4] [ -3]  [-2] [-1]

String single quote = 'Hello'
String double quote = "Hello"
String multiline = ''' Hello
                               Everyone
							   Thank you'''
							   
String Slicing: Division of String into several parts
Syntax = string_variable[start:stop:step]

Example 
Name = "Michael Jackson is the best dancer"
print(Name[0:16])

Name = "Michael Jackson is the best dancer"
print(Name[0:16:2])
'''
s = "hello world"
print(s[1]) #e
print(s[-1]) #d
print(s[1:3]) # el
print(s[1:-1]) # ello worl
print(s[:3]) # hel
print(s[2:]) # llo world
print(s[:-1]) # hello worl
print(s[::2]) # hlowrd
print(s[1::2]) # el ol
print(s[::-1]) # prints the string in reverse
