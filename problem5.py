# 5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

def countStrings(x):
    y = 0
    for string in x:
        if len(string) >= 2 and string[0] == string[-1]:
            y = y + 1
    return y

print(countStrings(['abc', 'xyz', 'aba', '1221']))