# 7. Write a Python program to remove duplicates from a list.
# rewrite a list as a set to remove duplicates

def removeDuplicates(x):
    my_set = set(x)
    return my_set
    
print(removeDuplicates([1, 2, 3, 2, 4, 1]))
