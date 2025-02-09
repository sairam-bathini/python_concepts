# AdjacentElementProduct

inputArray = list(map(int,input().split(",")))

print(inputArray)
length = len(inputArray)
new_array = []

def adjacentElementsProduct(inputArray):
    for i in range(length-1):
        product = inputArray[i] * inputArray[i+1]
        new_array.append(product)
    
    new_array.sort()
    print(new_array[-1])

adjacentElementsProduct(inputArray)
