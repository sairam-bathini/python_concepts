# Century from year
# input : 1905
# output : 20

import math 

year = int(input())

def centuryFromYear(year):
    century = math.ceil(year/100)
    
    return century

print(centuryFromYear(year))
