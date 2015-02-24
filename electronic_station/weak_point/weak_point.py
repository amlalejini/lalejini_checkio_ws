'''
Task:
The durability map is represented as a matrix with digits.
 Each number is the durability measurement for the cell.
 To find the weakest point we should find the weakest row and column. 
 The weakest point is placed in the intersection of these rows and columns. 
 Row (column) durability is a sum of cell durability in that row (column). 
 You should find coordinates of the weakest point (row and column). 
 The first row (column) is 0th row (column). 
 If a section has several equal weak points, then choose the top left point.
'''
LARGE_NUMBER = 999999999

def weak_point(matrix):
	row_sums = [sum(row) for row in matrix] # keep track of row sums
	col_sums = []
	for c in xrange(0, len(matrix[0])):		# calculate column sums
		col_sum = 0
		for r in xrange(0, len(matrix)):
			col_sum += matrix[r][c]
		col_sums.append(col_sum)

	min_row = 0 	# Keep track of minimum row number
	min_col = 0 	# Keep track of minimum col number

	# Search for minimum row
	for r in xrange(0, len(row_sums)):
		if row_sums[r] < row_sums[min_row]:
			min_row = r 
	# Search for minimum column
	for c in xrange(0, len(col_sums)):
		if col_sums[c] < col_sums[min_col]:
			min_col = c 
	# Weakest point is at the intersection of the min row and min col
	weakest_point = [min_row, min_col]
	return weakest_point


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(weak_point([[1]]), (list, tuple)), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"
