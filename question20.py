'''
Question 20
Level 3

Question:
Define a class with a generator which can iterate the numbers,
which are divisible by 7, between a given range 0 and n.

Hints:
Consider use yield

'''

# class
# function that can go through factors of seven(numbers divisible by 7: n%7)
# function takes a range as it's input (0, n)

# yield

class my_numbers():

    def sevens(self, x, n):
        num = xrange(x, n)
        l = []
        for item in num:
            if item == 0:
                continue
            elif item % 7 == 0:
                l.append(item)
#                yield item

            else:
                pass
        yield l

s = my_numbers()
print next(s.sevens(10, 100))
