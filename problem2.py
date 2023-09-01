# 2. Write a Python program to multiply all the items in a list.

def itemProduct(x):
    y = 1
    for i in x:
        y = y * i
    return y

print(itemProduct([1, 2, 3, 4, 5, 6]))
