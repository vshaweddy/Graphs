"""
Write a function that takes a 2D binary array and returns the number of 1 islands.

An island consists of 1s that are connected to the north, south, east or west. For example:

"""

islands: [[0, 1, 0, 1, 0],
          [1, 1, 0, 1, 0],
          [0, 0, 1, 0, 0],
          [1, 0, 1, 0, 0],
          [1, 1, 0, 0, 0]]


def dft_recursive(node, matrix, visited):

def island_counter(matrix);
    visited = set()

    # Iterate over every item
    for row in range(len(matrix[row])):
        for col in range(len(matrix[row])):
            # If it's a 1 and hasn't been visited
            item = matrix[row][col]
            if item == 1 and (row, col) not in visited:
                total_islands += 1
                visited.add((row, col))
                # Run a traversal
                dft_recursive((row, col), matrix, visited:)