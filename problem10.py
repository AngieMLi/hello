# 10. Write a Python program to find the list of words that are longer than n from a given list of words.

def listConditioned(x,n):
    y = []
    for i in x:
        if len(i) > n:
            y.append(i)
            
    print(y)
listConditioned(["apple", "pineapple", "grapefruit"], 6)
