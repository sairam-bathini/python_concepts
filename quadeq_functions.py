def roots_of_quadeq(a, b, c):
    d = (b*b) - 4*a*c
    root1 = (-b + (d**(0.5)))/ 2*a
    root2 = (-b - (d**(0.5)))/ 2*a
    return root1, root2

roots = roots_of_quadeq(1,2,3)
print(roots)
