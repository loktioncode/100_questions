'''
Question 15
Level 2

Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''

def numgen(num):
    num = num
    num2 = num * 2
    num3 = num * 3
    num4 = num * 4
    answer = int(num) + int(num2) + int(num3) + int(num4)
    print answer

num = raw_input("Enter a number ")
numgen(num)