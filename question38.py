'''
Question:
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half
values in one line and the last half values in one line.
'''

def tuple_printer():
    values = (1,2,3,4,5,6,7,8,9,10)
    halfway = len(values)/2
    print values[:halfway]
    print values[halfway:]

tuple_printer()