'''
Task:
You are given a text, which contains different english letters and punctuation symbols. You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

Input: A text for analysis as a string (unicode for py2.7).
Output: The most frequent letter in lower case as a string.
'''
from operator import itemgetter

def checkio(text):
	'''
	Calling this function accomplishes the task.
	'''
	data = text.lower()
	freq_dist = {}
	for char in data:
		if char.isalpha():
			if char in freq_dist.keys():
				freq_dist[char] += 1
			else:
				freq_dist[char] = 1
	freq_tuples = freq_dist.items()
	freq_tuples.sort(key = itemgetter(1))
	freq_tuples.reverse()

	highest_freqs = []
	top_freq = freq_tuples[0][1]
	for freq in freq_tuples:
		if freq[1] == top_freq:
			highest_freqs.append(freq)
		else:
			# because frequencies are sorted, can just break if we ever go lower than top
			break

	highest_freqs.sort() # sort on letters
	return highest_freqs[0][0]

    

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert checkio(u"Hello World!") == "l", "Hello test"
	assert checkio(u"How do you do?") == "o", "O is most wanted"
	assert checkio(u"One") == "e", "All letter only once."
	assert checkio(u"Oops!") == "o", "Don't forget about lower case."
	assert checkio(u"AAaooo!!!!") == "a", "Only letters."
	assert checkio(u"abe") == "a", "The First."
	print("Start the long test")
	assert checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
	print("The local tests are done.")