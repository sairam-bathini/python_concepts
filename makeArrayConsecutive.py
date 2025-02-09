statues = [int(i) for i in input().split(",")]

def makeArrayConsecutive2(statues):
    statues.sort()
    print(statues)
    length = len(statues)
    count = 0
    for i in range(length-1):
        diff = statues[i+1] - statues[i]
        if diff == 1:
            continue
        else:
            count = count + (diff-1)
        
    print(count)

makeArrayConsecutive2(statues)
