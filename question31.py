'''
Question:
Define a function which can print a dictionary where the keys are numbers between
1 and 3 (both included) and the values are square of keys.

Hints:

Use dict[key]=value pattern to put entry into a dictionary.
Use ** operator to get power of a number.
'''

d = {} # OR d = dict()

def doubler(d):
    x = range(1, 4)
    for item in x:
        d[item] = item ** 2
    return d


print doubler(d)