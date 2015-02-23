#!/usr/bin/python

from Queue import PriorityQueue

start_square = (1, 1)
goal_square = (10, 10) # Goal is row - 2, col - 2

fringe = None	 # The fringe holds tuples of nodes with their f-value (cost + heuristic in A*): (f-value, Search_Node)
expanded = []    # List of already expanded nodes in current search

class Node(object):
	def __init__(self, node_id, parent, cost, heuristic):
		self.parent = parent		# Pointer to this node's parent
		self.node_id = node_id		# Grid point (x, y) of this node
		self.cost = cost			# Cost to get to this node
		self.h = heuristic 			# Heuristic value at this node

def manhattan_distance(a, b):
	'''
	This function returns the Manhattan distance between two grid squares.
	a: (x1, y1)
	b: (x2, y2)
	'''
	return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_successors(maze_map, position):
	'''
	This function returns the valid successor search nodes given a position in the map.
	'''
	current_row = position[0]
	current_col = position[1]
	# Enumerate possible successors locations
	successor_candidates = [(current_row + 1, current_col), (current_row, current_col + 1), 
							(current_row, current_col - 1), (current_row - 1, current_col)] # South, east, west, north
	successors = []
	# Only add the valid successors
	for s in successor_candidates:
		if valid_position(maze_map, s):
			successors.append(s)
	
	return successors

def valid_position(maze_map, position):
	'''
	Given a position and a map, this function returns true if position is valid and false otherwise.
	'''
	# Check if within bounds of map
	try:
		maze_map[position[0]][position[1]]
	except:
		# Not a within the bounds of the map
		return false

	# Check if not a bush (1)
	return maze_map[position[0]][position[1]] == 0


def get_f_value(node):
	'''
	This function takes a node as input and output that node's f-value.
	The f-value is used to determine the order in which nodes in the fringe are expanded.
	Lower f-values are expanded first.

	Greedy search: f-value = heuristic value 
	Uniform cost search: f-value = cost to reach node 
	A*: f-value = heuristic + cost 
	'''
	return node.h + node.cost 

def search(maze_map):
	'''
	This function performs an A* search for a path from the starting location to the goal location.
	Returns the goal node.
	A path can be extracted given the goal node by following parent pointers in each node starting with the goal node.
	'''
	total_expansions = 0 		# Keep a count of total number of expansions
	
	while not fringe.empty():
		# grab the next node to expand (remember it is stored as (f-value, node))
		item_to_expand = fringe.get()
		node_to_expand = item_to_expand[1]

		# Only expand this node if it has not been expanded before
		if node_to_expand.node_id not in expanded:
			total_expansions += 1

			# Test to see if we're at our goal
			if node_to_expand.node_id == goal_square:
				print ("Found the goal after " + str(total_expansions) + " expansions")
				print ("Cost of final path found: " + str(node_to_expand.cost))
				return node_to_expand

			# Add this node to expanded list
			expanded.append(node_to_expand.node_id)

			# Get node's successors
			successors = get_successors(maze_map, node_to_expand.node_id)

			# For each successor:
			for s in successors:
				# Calculate cost to get from expanded node to this successor
				cost = node_to_expand.cost + 1
				# Calculate this successor's heuristic value
				h = manhattan_distance(s, goal_square)
				# Create successor node
				successor_node = Node(node_id = s, parent = node_to_expand, cost = cost, heuristic = h)
				# Get the node's f-value
				f_value = get_f_value(successor_node)
				# Add successor node to fringe
				fringe.put((f_value, successor_node))

	print("No path was found after %d expansions" % (total_expansions))

	return None

def extract_directions_from_path(maze_map, path):
	'''
	Given a map and a path, this function will extract the directions necessary to take the path (N, S, E, W)
	'''
	directions = ""
	for i in xrange(0, len(path) - 1):
		# For readability, expand out row col stuff
		row1 = path[i][0]
		col1 = path[i][1]
		row2 = path[i + 1][0]
		col2 = path[i + 1][1]
		direction = None
		if row2 == (row1 + 1):
			direction = "S"
		elif row2 == (row1 - 1):
			direction = "N"
		elif col2 == (col1 + 1):
			direction = "E"
		elif col2 == (col1 - 1):
			direction = "W"
		directions += direction
	return directions



def checkio(maze_map):
	'''
	Calling this function accomplishes the task.
	'''
	global fringe, expanded

	# Assert that Start/goal position is valid square
	assert valid_position(maze_map, start_square), "Start Position is not a valid position!"
	assert valid_position(maze_map, goal_square), "Goal Position must be a valid position!"

	# Initialize Starting Square as a search node
	start_node = Node(node_id = start_square, parent = None, cost = 0, heuristic = manhattan_distance(start_square, goal_square))

	# Initialize fringe with starting square
	fringe = PriorityQueue()
	fringe.put((get_f_value(start_node), start_node))
	
	# Clear out expanded list
	expanded = []

	# Run A* Search for goal square
	print("=============================")
	print("Starting search from map location: " + str(start_node.node_id))
	print("My goal is: " + str(goal_square))
	print("My starting f-value: " + str(get_f_value(start_node)))
	goal_node = search(maze_map)
	if goal_node == None:
		print("Could not find a path.")
		return None
	
	# Extract path by backtracking starting at goal node and moving from parent to parent until we hit the start node
	path = []
	current_node = goal_node
	while current_node != None:
		path.append(current_node.node_id)
		current_node = current_node.parent
	path.reverse()

	print("Path: " + str(path))
	# Translate our found path into the correct format for the task (string of directions)
	directions = extract_directions_from_path(maze_map, path)
	print("Path directions: " + str(directions))
	return directions



if __name__ == "__main__":
	#This code using only for self-checking and not necessary for auto-testing
	def check_route(func, labyrinth):
		MOVE = {"S": (1, 0), "N": (-1, 0), "W": (0, -1), "E": (0, 1)}
		#copy maze
		route = func([row[:] for row in labyrinth])
		pos = (1, 1)
		goal = (10, 10)
		for i, d in enumerate(route):
			move = MOVE.get(d, None)
			if not move:
				print("Wrong symbol in route")
				return False
			pos = pos[0] + move[0], pos[1] + move[1]
			if pos == goal:
				return True
			if labyrinth[pos[0]][pos[1]] == 1:
				print("Player in the pit")
				return False
		print("Player did not reach exit")
		return False

	# These assert are using only for self-testing as examples.
	assert check_route(checkio, [
	    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
	    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
	    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
	    [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
	    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
	    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
	    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
	    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
	    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "First maze"
	assert check_route(checkio, [
	    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Empty maze"
	assert check_route(checkio, [
	    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
	    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
	    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
	    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
	    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
	    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
	    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
	    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
	    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
	    [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
	    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Up and down maze"
	assert check_route(checkio, [
	    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
	    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
	    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
	    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
	    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
	    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
	    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
	    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
	    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
	    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
	    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Dotted maze"
	assert check_route(checkio, [
	    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
	    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
	    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
	    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
	    [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
	    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
	    [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
	    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
	    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
	    [1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
	    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Need left maze"
	assert check_route(checkio, [
	    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
	    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
	    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
	    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
	    [1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
	    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
	    [1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
	    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
	    [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
	    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "The big dead end."
	print("The local tests are done.")
