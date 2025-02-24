given_word = input()
vowels = 'aeiou'
count = 0
find_vowels = []

for i in given_word:
    for j in vowels:
        if i == j:
            find_vowels.append(i)
        else:
            continue

print(find_vowels)
