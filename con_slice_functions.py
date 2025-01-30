'''
Define a list and string
---------------------------------------
Use Mnemonics & Keywords
---------------------------------------
Slicing → “Cut a piece” → list[start:end]
Concatenation → “Join together” → list + another_list
Repetition → “Repeat multiple times” → list * n
Finding Index → “Search first occurrence” → index()
Sorting → “Arrange in order” → sorted(list, reverse=True)
'''
panch_pandav = ['yudhister', 'bheem', 'arjun', 'nakul', 'sahadev']
about_pandav = "They are the sons of kunti devi and pandu"

concatenate_pandav = panch_pandav + ['draupathi']  # concatenate an element in list

concantenate_about_pandav = about_pandav + ' ji'  # concatenate a string

kunti_putra = panch_pandav[0:3]  # slice a list

who_are_they = about_pandav[0:31]  # slice a string

panch_pandav.append('krishna')  # append a string

repeat_panch_pandav = panch_pandav * 2

is_arjun_there = 'arjun' in panch_pandav

print(sorted(panch_pandav))  # print sorted elements
print(who_are_they)  # print sliced string
print(concatenate_pandav)  # print concatenate list
print(concantenate_about_pandav)  # print concatenate string
print(repeat_panch_pandav)
print(is_arjun_there)
