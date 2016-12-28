'''
fine a function which can generate a list where the values are square of numbers
between 1 and 20 (both included). Then the function needs to print all values
except the first 5 elements in the list.

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list
'''

def list_print():
    list_ = list()
    for item in range(1, 21):
        list_.append(item ** 2)
    return list_[5:]

print list_print()