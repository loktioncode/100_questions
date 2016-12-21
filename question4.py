'''
#----------------------------------------#
Question 4
Level 1

Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple
'''
def list_producer(usr_input=None):

    #string_input = raw_input("Enter numbers: ")
    string_input = usr_input
    input_list = string_input.split(",")
    #input_list = [int(a) for a in input_list]
    print input_list
    print tuple(input_list)

if __name__ == "__main__":
    list_producer()