'''
Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

user_input = raw_input("Enter text ")
letters = 0
digits = 0

for character in user_input:
    if character.isalpha():
        letters += 1

    elif character.isdigit():
        digits += 1

print "LETTERS: %s\nDIGITS: %s" %(letters, digits)
