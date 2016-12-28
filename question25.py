'''
Question 25
Level 1

Question:
    Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later
'''

class Person(object):
    name = "Person"

    def __init__(self, name=None):
        self.name = name

vuyisile = Person()
vuyisile.name = "Vuyisile"

print "%s's name is %s" % (Person.name, vuyisile.name)