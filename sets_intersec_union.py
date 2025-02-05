# Sample input: set A = {1,2,3,4,5}
#               set B = {4,5,6}
# Sample output: Intersection:{4,5}
#                Union:{1,2,3,4,5,6}

setA = {int(i) for i in in,put().split(",")}
setB = {int(i) for i in input().split(",")}

intersection = setA.intersection(setB)
union = setA.union(setB)

print(f"Intersection:{intersection}")
print(f"Union:{union}")
