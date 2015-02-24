#!/usr/bin/python

'''
Task:
For this mission, you are given a non-empty array of natural numbers (X). 
 With it, you must separate the upper half of the numbers from the lower half
 and find the median.
Input: An array as a list of integers.
Output: The median as a float or an integer.
'''

def verbose_checkio(data):
	'''
	This function accomplishes the task.
	'''
	data.sort()
	median = None
	if len(data) % 2 == 0:
		# even
		median = (data[len(data)/2 - 1] + data[len(data)/2]) / 2.0
	else:
		# odd
		median = data[int(len(data)/2)]
	return median

def checkio(data):
	'''
	This function accomplishes the task.
	'''
	data.sort()
	return (data[int(len(data)/2 - 1)] + data[int(len(data)/2)]) / 2.0 if len(data) % 2 == 0 else data[int(len(data)/2)]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
	assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
	assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
	assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
	print("Start the long test")
	assert checkio(list(range(1000000))) == 499999.5, "Long."
	print("The local tests are done.")
	checkio([3,6,20,99,10,15])