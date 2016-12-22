'''
Question 16
Level 2

Question:
Use a list comprehension to 1) print odd numbers and the square of each odd number in a list. The list is input by a sequence of
comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9

'''

response = raw_input("Enter a comma separated list of numbers ")
response_list = response.split(",")
list_of_numbers = []
for item in response_list:
    list_of_numbers.append(int(item))

answer = [item for item in list_of_numbers if item % 2 != 0]
answer_squared = [item**2 for item in answer]
print "The following numbers are odd", answer
print "And this is a list of the square of each odd number", answer_squared

