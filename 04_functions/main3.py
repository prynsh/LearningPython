import math
def value(r):
    area = math.pi * r ** 2
    circumference = 2 * math.pi * r
    return area, circumference

result = value(4) 
print(math.trunc(result))
