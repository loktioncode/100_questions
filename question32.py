'''
Question:
Define a function which can print a dictionary where the keys are
numbers between 1 and 20 (both included) and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
Use range() for loops.
'''

def super_function():
    d = dict()
    x = range(1, 21)
    for item in x:
        d[item] = item ** 2
    return d

print super_function()