#4. Write a Python program to get the smallest number from a list.

def findSmallestNumber(x):
    x.sort()
    return(x[0])
    
print(findSmallestNumber([6, 2, 3, 4, 5, 1]))
