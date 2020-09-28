"""
Write a function that takes a 2D binary array and returns the number of 1 islands.

An island consists of 1s that are connected to the north, south, east or west. For example:

islands: [[0, 1, 0, 1, 0, 0],
          [1, 1, 0, 1, 1, 0],
          [0, 0, 1, 0, 0, 0],
          [1, 0, 1, 0, 0, 0],
          [1, 1, 0, 0, 0, 0]]
"""

class Stack():
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)

def get_neighbors(row, col, island_matrix):
    neighbors = []
    # Check the neighbor above row and col
    if row > 0 and island_matrix[row - 1][col] == 1:
        neighbors.append ((row - 1, col))
    # Check the neighbor below row and col
    if row < len(island_matrix) - 1 and island_matrix[row + 1][col] == 1:
        neighbors.append((row + 1, col))
    # Check the neighbor left row and col
    if col > 0 and island_matrix[row][col - 1] == 1:
        neighbors.append((row, col - 1))
    # Check the neighbor right row and col
    if col < len(island_matrix[row]) - 1 and island_matrix[row][col + 1] == 1:
        neighbors.append((row, col + 1)) 
    return neighbors

def dft(starting_row, starting_col, island_matrix, visited):
    # Create an empty stack
    stack = Stack()
    # Push the starting row and col onto stack
    stack.push((starting_row, starting_col))
    # While stack is not empty:
    while stack.size() > 0:
        # Pop the current row and col off the stack
        current_row_col = stack.pop()
        row = current_row_col[0]
        col = current_row_col[1]
        # if the current row and col NOT visited:
        if visited[row][col] is False:
            # Set the current row and col as visited
            visited[row][col] = True
            # get the neighbor row and columns
            for neighbor in get_neighbors(row, col, island_matrix):
                # push them onto the stack
                stack.push(neighbor)

def island_counter(island_matrix):
    # Keep track of all visited vertices
    visited_matrix = []
    for i in range(len(island_matrix)):
        visited_matrix.append([False] * len(island_matrix[0]))

    island_count = 0
    # Walk through each cell of the matrix
    for row in range(len(island_matrix)):
        for col in range(len(island_matrix[row])):
            # If a cell value is 1 and has not been visited
            if island_matrix[row][col] == 1 and visited_matrix[row][col] is False:
            # Traverse the connected component (graph)
                # DFT starting at the current cell
                dft(row, col, island_matrix, visited_matrix)
                # Once we are done DFT, that means we have found a new island
                # Increment some island_count value + 1
                island_count += 1
    return island_count


islands = [[0, 1, 0, 1, 0, 0],
          [1, 1, 0, 1, 1, 0],
          [0, 0, 1, 0, 0, 0],
          [1, 0, 1, 0, 0, 0],
          [1, 1, 0, 0, 0, 0]]

print(island_counter(islands))