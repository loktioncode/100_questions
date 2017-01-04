'''
Question:

Assuming that we have some email addresses in the "username@companyname.com" format,
please write program to print the user name of a given email address.
Both user names and company names are composed of letters only.
Example:
If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

john

In case of input data being supplied to the question, it should be assumed to be a console input.

'''
import re

email_addr = raw_input("Enter email address ")
# email_addr = "vuyisile@mozilla.com"
result = re.search(r'(\w+)@(\w+)((\.)+(\w+))', email_addr)
print "You are ", result.group(1)
print "You work for", result.group(2)
print "Your company uses a", result.group(3), "domain"