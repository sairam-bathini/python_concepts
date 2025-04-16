from collections import Counter

def anagram(str1, str2):
    # Convert to lowercase and remove spaces
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Count character frequency and compare
    return Counter(str1) == Counter(str2)

# Example usage
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

print(anagram(string1, string2))
