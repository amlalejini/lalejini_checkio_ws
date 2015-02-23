#!/usr/bin/python
import re

'''
Task:
Verify safety of password.
Safe password -- len >= 10 symbols, at least 1 digit, at least 1 upper case, at least 1 lower case
Input: A password as a string
Output: Is the password safe or not (safety defined above)?
'''

def checkio_compiled_re(data):
	'''
	This function accomplishes the task using regular expressions.
	'''
	lower_case_check = re.compile(".*[a-z]+.*")
	upper_case_check = re.compile(".*[A-Z]+.*")
	digit_check		 = re.compile(".*[0-9]+.*")

	lower_case_pass = lower_case_check.match(data) != None
	upper_case_pass = upper_case_check.match(data) != None
	digit_pass 		= digit_check.match(data) != None
	len_pass 		= len(data) >= 10

	print "============="
	print data
	print "Lower Case Check: ", lower_case_pass
	print "Upper Case Check: ", upper_case_pass
	print "Digit Check: ", digit_pass
	print "Length Check: ", len_pass
	return lower_case_pass and upper_case_pass and digit_pass and len_pass

def checkio(data):
	'''
	This function accomplishes the task using regular expressions.
	'''
	lower_case_pass = re.search("[a-z]", data) != None  # Check for a lower case letter
	upper_case_pass = re.search("[A-Z]", data) != None  # Check for an upper case letter
	digit_pass 		= re.search("[0-9]", data) != None  # Check for a digit
	length_pass 	= len(data) >= 10		            # Check length of data

	print "============="
	print data
	print "Lower Case Check: ", lower_case_pass
	print "Upper Case Check: ", upper_case_pass
	print "Digit Check: ", digit_pass
	print "Length Check: ", length_pass
	return lower_case_pass and upper_case_pass and digit_pass and length_pass


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    checkio('A1213pokl')
    checkio('bAse730onE4')
    checkio('asasasasasasasaas')
    checkio('QWERTYqwerty')
    checkio('123456123456')
    checkio('QwErTy911poqqqq')