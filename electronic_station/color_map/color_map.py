'''
Task:
when given any separation of a plane into contiguous regions and producing a figure called a map, no more than four colors are required to color the regions of the map so that no two adjacent regions have the same color. Two regions are called adjacent if they share a common boundary that is not a corner, where corners are the points shared by three or more regions. For our model we will use a grid with square cells.
You are given a regional map as a grid (matrix). There are N countries located on this map. Each country has a number from 0 to N-1. Two cells are adjacent if they have a common edge. Each country has one or more cells that are connected. Thus you can move between any cells of the country X just using for this adjacent cells. 
Each cell is marked by the number of its designated country.
You should "color" a map with 4 colors. All of the cells comprising one country should be one color. Adjacent cells of various countries should not have the same color.
The result should be represented as a sequence of numbers 1,2,3 or 4. Each element shows the color of its country matching the index. For example, the 0th element shows the color of country 0. So the result should have N elements.
'''


##### Precondition: Country numbers are in sequence from 0 to N-1
import random


COLORS = 4	# Total number of colors
MAX_STEPS = 1000

class Node(object):
	'''
	Represents a 'country' in the map graph.
	'''
	def __init__(self, node_id = None, color_assignment = None, adjacents = None, map_positions = None):
		self.node_id = node_id
		self.color_assignment = color_assignment	# Store color assignment
		self.adjacents = adjacents 					# Store list of adjacent nodes or countries
		self.map_positions = map_positions			# Store list of locations occupied by this node in the map

def map_to_graph(tup_map):
	'''
	Converts map (tuple of tuples) to a graph (network of nodes).
	'''
	# Get the number of unique countries in the region
	# 	- Flatten map, get unique countries
	flat_map = [val for tup in tup_map for val in tup]
	unique_regions = []
	for val in flat_map:
		if val not in unique_regions:
			unique_regions.append(val)

	# Create empty graph with correct number of regions
	graph = [Node(node_id = n, color_assignment = None, adjacents = [], map_positions = []) for n in xrange(0, len(unique_regions))]

	# Populate map positions for each node (map positions a particular country occupies)
	# Also populate adjecent regions for each node
	for r in xrange(0, len(tup_map)):
		for c in xrange(0, len(tup_map[r])):
			graph[tup_map[r][c]].map_positions.append((r,c))
			neighbors = get_neighbors(tup_map, (r,c))
			for neighbor in neighbors:
				if neighbor not in graph[tup_map[r][c]].adjacents:
					graph[tup_map[r][c]].adjacents.append(neighbor)

	return graph

def get_neighbors(tup_map, loc):
	'''
	Given a position, get any neighboring regions to that position that are different 
	 from the given region.
	'''
	region = tup_map[loc[0]][loc[1]]
	coords = [(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] + 1), (loc[0], loc[1] - 1)]
	neighbors = []
	for c in coords:
		valid_location = (c[0] >= 0 and c[0] < len(tup_map)) and (c[1] >= 0 and c[1] < len(tup_map[0]))
		if valid_location and tup_map[c[0]][c[1]] != region and tup_map[c[0]][c[1]] not in neighbors:
			neighbors.append(tup_map[c[0]][c[1]])
	return neighbors

def conflicts(node, color, graph):
	'''
	The CONFLICTS function counts the number of constraints violated by a particular value,
	 given the rest of the current assignment.
	'''
	conflicts = 0
	adjacent_colors = [graph[region].color_assignment for region in node.adjacents]
	for adj_color in adjacent_colors:
		if color == adj_color:
			conflicts += 1
	return conflicts

def print_node(node):
	print("Node ID: " + str(node.node_id))
	print("Color: " + str(node.color_assignment))
	print("Adjacent Nodes: " + str(node.adjacents))
	print("Map Positions: " + str(node.map_positions))

def constraint_satisfaction_search(tup_map):
	'''
	Given a map (a tuple of tuples), returns colored graph such that no adjacent regions are 
	 the same color.
	'''
	# Step 1: Map -> Graph
	graph = map_to_graph(tup_map)

	# Step 2: Assign Colors randomly
	for node in graph:
		node.color_assignment = random.randint(0, COLORS - 1)

	# print("=== BEFORE ===")
	# for node in graph:
	# 	print("===============")
	# 	print_node(node)
	# 	print("Conflicts for node %d: %d" % (node.node_id, conflicts(node, node.color_assignment, graph)))

	# Step 3: Begin Local search
	# - Repeat
	#	- Get all constraint violations
	# 	- If constraints (no violations) are met => return current assignments
	# 	- Select a random node with a constraint violation
	# 	- Select color assignment that minimizes conflicts 
	#	- Set node's color assignment to selected color
	steps = 0
	while (steps < MAX_STEPS):
		naughty_nodes = []
		# Get all constraint violations
		for node in graph:
			if conflicts(node, node.color_assignment, graph) != 0:
				naughty_nodes.append(node.node_id)
		# If no violations, return current assignments
		if len(naughty_nodes) == 0:
			# print("=== AFTER ===")
			# print("Number of steps: " + str(steps))
			# for node in graph:
			# 	print("===============")
			# 	print_node(node)
			# 	print("Conflicts for node %d: %d" % (node.node_id, conflicts(node, node.color_assignment, graph)))
			return graph
		# Select a random node with a constraint violation
		lucky_winner = naughty_nodes[random.randint(0, len(naughty_nodes) - 1)]
		# Select color assignment for lucky_winner that minimizes conflicts
		min_conflict_color = (-1, -1) # Color, conflicts
		for c in xrange(0, COLORS):
			num_conflicts = conflicts(graph[lucky_winner], c, graph)
			if min_conflict_color[0] == -1:
				min_conflict_color = (c, num_conflicts)
			elif min_conflict_color[1] > num_conflicts:
				min_conflict_color = (c, num_conflicts)
		# Set node's color assignment to selected color
		graph[lucky_winner].color_assignment = min_conflict_color[0] 
		steps += 1
	return None

def color_map(region):
	graph = constraint_satisfaction_search(region)
	while graph == None:
		graph = constraint_satisfaction_search(region)
	return [node.color_assignment + 1 for node in graph]

if __name__ == "__main__":
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assignment = color_map(((7,4,4,4,),(7,0,1,5,),(7,2,3,5,),(6,6,6,5,),))
	print(str(assignment))

	

	