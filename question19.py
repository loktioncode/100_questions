'''
Question 19
Level 3

Question:
You are required to write a program to sort the (name, age, height)
tuples by ascending order where name is string, age and height are numbers. The tuples are input by console.
The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
'''

# get tuples from console
# tuple[0]= string, tuple[1] = digit, tuple[2]= digit
# sort tuples by name, age and then height.
# people = [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

people = []
while True:
    l = raw_input("Enter tuples ")
    if not l:
        break
    people.append(tuple(l.split(",")))
print sorted(people, key=lambda item: (item[0], item[1], item[2]))

## Solution 2, using itemgetter
# from operator import itemgetter, attrgetter
# people = []
# while True:
#    l = raw_input("Enter tuples")
#    if not l:
#        break
#    people.append(tuple(l.split(",")))
# print sorted(people, key=itemgetter(0,1,2))
# if the object you are required to sort is a sequence and has named attributes, use attrgetter