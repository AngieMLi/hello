# 11. Write a Python function that takes two lists and returns True if they have at least one common member.

def commonMember(x, y):
    for i in x:
        if i in y:
            return True
    return False
    
print(commonMember([1, 2, 3, 4], [4, 5, 6, 7]))