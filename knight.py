"""
Poushali Ramead
Task 1 - AAI 3
"""

# Initialise variables that have to be tracked - global, goal variables
shortest_num_moves = 100000
shortest_path = []
num_nodes_visited = 0

def main():
    # global variables
    global shortest_num_moves, shortest_path, num_nodes_visited

    # user input and validation
    start_position, target_position = user_input()
    current_position = start_position

    # Initialise variables that have to be tracked local, during recursion
    current_num_moves = 0 
    current_path = [current_position]

    # Start the recursive search by calling recursive function knight_shortest_path
    knight_shortest_path(current_position, target_position, current_num_moves, current_path)

    print(f"number of moves: {shortest_num_moves}, number of nodes visited during search: {num_nodes_visited}, position: {target_position}")
    print(print_path())
    print(f"From position {start_position} to {target_position}, {shortest_num_moves} moves is needed")
    

# User input and validation of input
# returns start_position and target_position back to main
def user_input():
    while True:
        print("Starting Position")
        x_start = int(input("x_start: "))
        y_start = int(input("y_start: "))

        print("Target Position")
        x_target = int(input("x_target: "))
        y_target = int(input("y_target: "))
    
        if ((0 <= x_start <= 7) and (0 <= y_start <= 7) and (0 <= x_target <= 7) and (0 <= y_target <= 7)):
            break
        else:
            print("Positions should be within the range 0 to 7")

    return (x_start, y_start), (x_target, y_target)


# main recursion function
def knight_shortest_path(current_position, target_position, current_num_moves, current_path):
    global shortest_num_moves, shortest_path, num_nodes_visited
    
    num_nodes_visited = num_nodes_visited + 1

    # if the current path is already the same or greater than the shortest path found so far, no need to explore further
    if current_num_moves >= shortest_num_moves:
        return
    
    # base case, if target_position reached
    if current_position == target_position:
        shortest_num_moves = current_num_moves
        shortest_path = list(current_path)
        return
    
    # executed if none of the above if statements were executed. recursive
    # at the given position, the next positions are generates using helper function knight_next_moves
    # knight_next_moves already calls appropriate function, filters out visited positions, and sorts the lists according to 
    # Manhattan distance heuristic
    next_moves = knight_next_moves(current_position, current_path, target_position)
    for move in next_moves:
        current_path.append(move)
        knight_shortest_path(move, target_position, current_num_moves + 1, current_path)
        # backtracking
        current_path.pop()                  


# As a way to improve results, manhattan distance is used here as a heuristic
# Once next moves of the knight are generated given a position, they are then sorted in the order of how close they are to the target
# this is done as a mean to improve the number of nodes variable

# knight_moves returns the possible valid knight moves given a position of the knight on the board
# it filters out already visited positions
# it sorts the list of available moves based on the heuristic
def knight_next_moves(current_position, current_path, target_position):
    x, y = current_position
    next_moves = calculate_moves(x, y)
    next_moves = filter_moves(next_moves, current_path)
    next_moves = sort_moves(next_moves, target_position)
    return next_moves


# given a position x,y calculates the next possible moves using the following method
# delta_x, delta_y is an element of {(-1, -2), (-2, -1), (1, -2), (-1, 2), (2, -1), (-2, 1), (1, 2), (2, 1)}
def calculate_moves(x, y):
    next_moves = [
        (x - 1, y - 2),
        (x - 2, y - 1),
        (x + 1, y - 2),
        (x - 1, y + 2),
        (x + 2, y - 1),
        (x - 2, y + 1),
        (x + 1, y + 2),
        (x + 2, y + 1),
    ]
    return next_moves

# filters out invalid moves calculated and positions already visited
# the variable current_path holds the positions alraedy visited up until that point
def filter_moves(next_moves, current_path):
    updated_next_moves = []
    for move in next_moves:
        if (move[0] <= 7 and move[0] >= 0) and (move[1] <= 7 and move[1] >= 0) and move not in current_path:
            updated_next_moves.append(move)
    return updated_next_moves

# manhattan distance heuristic
def sort_moves(next_moves, target_position):
    return sorted(next_moves, key=lambda move: manhattan(move, target_position))

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
# print shortest path, called in main
def print_path():
    global shortest_path

    path_string = ""
    for i in range(len(shortest_path)):
        path_string = path_string + str(shortest_path[i])
    
        # If it is not the last item, an arrow is placed in between
        if i < len(shortest_path) - 1:
            path_string = path_string + " -> "

    return path_string


main()
