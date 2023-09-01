# 1. Write a Python program to sum all the items in a list.

def itemSum(x):
    y = 0
    for i in x:
        y = y + i
    return y
    
print(itemSum([1, 2, 3, 4, 5, 6]))
