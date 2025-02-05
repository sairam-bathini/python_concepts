# sets

winner_set = {'NTR', 'ANR', 'RAM', 'NITIN'}
runner_set = {'NTR', 'AKHIL', 'TARUN', 'MAHESH'}

intersection_set = runner_set.intersection(winner_set)
print(intersection_set) #output NTR (it is the common element from both the sets

union_set = runner_set.union(winner_set)
print(union_set) #combines both the sets and prints the both the elements in the set by removing duplicates

difference_set = runner_set.difference(winner_set)
print(difference_set) # removes the common elements from the runner set and print the unique elements

difference_set = winner_set.difference(runner_set)
print(difference_set)

symmetric_diff_set = winner_set.symmetric_difference(runner_set)
print(symmetric_diff_set)
