# grid cells: (row, col)
NEIGHBORS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def get_neighbor_cells(grid, position):
    '''
    Given a grid and a position, this function returns a list of all neighboring cells.
    '''
    surroundings = []
    for n in NEIGHBORS:
        candidate_loc = (position[0] + n[0], position[1] + n[1])
        valid_location = (candidate_loc[0] >= 0 and candidate_loc[0] < len(grid)) and (candidate_loc[1] >= 0 and candidate_loc[1] < len(grid[-1]))
        if valid_location:
            surroundings.append(candidate_loc)
    return surroundings


def count_neighbours(grid, row, col):
    '''
    This function accomplishes the task.
    '''
    neighbor_locs = get_neighbor_cells(grid, (row, col))
    neighbor_count = 0
    for loc in neighbor_locs:
        if grid[loc[0]][loc[1]] == 1:
            neighbor_count += 1

    print("=========")
    print("Neighbor Locs: " + str(neighbor_locs))
    print("Neighbor Count: " + str(neighbor_count))
    return neighbor_count



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
