# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

def specifiedList(x):
    del x[0]
    del x[4-1]
    del x[5-1]
    return x

print(specifiedList([1, 2, 3, 4, 5, 6, 7, 8]))