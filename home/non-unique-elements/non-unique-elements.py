#!/usr/bin/python

'''
Task:
You are given a non-empty list of integers (X). 
For this task, you should return a list consisting of only the non-unique elements in this list.
To do so you will need to remove all unique elements (elements which are contained in a given list only once).
 When solving this task, do not change the order of the list. Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].
'''

def checkio(data):
	'''
	Calling this function accomplishes the task.
	'''
	freq_dist = {}  # This will contain frequency distribution of elements in data
	non_unique = []
	unique = []
	for element in data:
		# if this is the first time we see an element
		if not (element in freq_dist.keys()):
			# add the element to freq distribution and set its count to zero
			freq_dist[element] = 1
		else:
			freq_dist[element] += 1
	for element in data:
		if freq_dist[element] > 1:
			non_unique.append(element)
		else:
			unique.append(element)
	print("================")
	print("Original list: " + str(data))
	print("Frequency Distribution: " + str(freq_dist))
	print("Unique elements: " + str(unique))
	print("Non-Unique elements: " + str(non_unique))
	return non_unique

if __name__ == "__main__":
	 #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(checkio([1]), list), "The result must be a list"
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"
