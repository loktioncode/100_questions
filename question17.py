'''
Question 17
Level 2

Question:
Write a program that computes the net amount of a bank account
based a transaction log from console input.
 The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
import re


balance = 0
abort = False

while abort == False:

    user_input = raw_input("Enter Transaction. XX to quit ")
    if user_input == "XX":
        abort = True
        quit()
    amount = int(user_input[2:len(user_input)])
    deposit = re.compile(r'[dD]\s\d+')
    withdrawal = re.compile(r'[wW]\s\d+')



    if deposit.match(user_input):
        balance += amount
        print "Account Balance : $%r" % balance

    elif withdrawal.match(user_input):
        if amount > balance:
            print "Amount exceeds available balance"
            quit()
        balance -= amount
        print "Account Balance : $%r" % balance


    else:
        print "Regex did not match anything"
