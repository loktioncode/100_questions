'''
Question 14
Level 2

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

'''

cases = {"UPPER_CASE":0, "LOWER_CASE":0}
user_input = raw_input("Enter text ")
for word in user_input:
    if word.isupper():
        cases["UPPER_CASE"] += 1
    elif word.islower():
        cases["LOWER_CASE"] += 1
    else:
        pass
print "Upper Case Letters", cases["UPPER_CASE"]
print "Lower Case Letters", cases["LOWER_CASE"]