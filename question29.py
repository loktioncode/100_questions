'''
Question:
Define a function that can accept two strings as input and print the
string with maximum length in console. If two strings have the same length,
then the function should print all strings line by line.

Hints:
'''

def converter(x, y):
    if len(x) > len(y):
        print x
    elif len(y) > len(x):
        print y
    else:
        print x,"\n", y
