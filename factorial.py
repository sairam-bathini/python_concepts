# input N = 5
# output Factorial of 5!= 120

N = int(input())
i=0
fact= 1
while i<N:
    fact = fact * (N-i)
    i +=1

print(f"Factorial of {N}!={fact}")
