import sys
sys.path.append("../")
from Session import getSessionId
from aocd import get_data, submit

session_id = getSessionId()

data = get_data(session=session_id, day=4, year=2024).splitlines()

def count_word_in_matrix(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])
    word_len = len(word)
    count = 0
    
    # Directions for 8 possible movements (right, left, down, up, and diagonals)
    directions = [
        (0, 1),  # Right
        (0, -1),  # Left
        (1, 0),  # Down
        (-1, 0),  # Up
        (1, 1),  # Down-right (diagonal)
        (-1, -1),  # Up-left (diagonal)
        (1, -1),  # Down-left (diagonal)
        (-1, 1)  # Up-right (diagonal)
    ]
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    # Function to check the word in a specific direction
    def check_direction(x, y, dx, dy):
        for i in range(word_len):
            new_x = x + i * dx
            new_y = y + i * dy
            if not is_valid(new_x, new_y) or matrix[new_x][new_y] != word[i]:
                return False
        return True
    
    # Iterate over every cell in the matrix
    for i in range(rows):
        for j in range(cols):
            # For each direction, check if the word starts at matrix[i][j]
            for dx, dy in directions:
                if check_direction(i, j, dx, dy):
                    count += 1
    
    return count


def Part1():
    
    return count_word_in_matrix(data, "XMAS")
                
def count_x_mas_all_orientations(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    count = 0
    matches = []

    for i in range(1, rows - 1):  # Avoid the top and bottom edges
        for j in range(1, cols - 1):  # Avoid the left and right edges
            if grid[i][j] == 'A':  # Check center 'A'
                # Orientation 1: M0M (top-left and top-right), S0S (bottom-left and bottom-right)
                if (grid[i - 1][j - 1] == 'M' and grid[i - 1][j + 1] == 'M' and
                    grid[i + 1][j - 1] == 'S' and grid[i + 1][j + 1] == 'S'):
                    count += 1
                    matches.append((i, j, "Orientation 1"))

                # Orientation 2: M0S (top-left and bottom-right), S0M (top-right and bottom-left)
                if (grid[i - 1][j - 1] == 'M' and grid[i + 1][j + 1] == 'S' and
                    grid[i - 1][j + 1] == 'S' and grid[i + 1][j - 1] == 'M'):
                    count += 1
                    matches.append((i, j, "Orientation 2"))

                # Orientation 3: S0S (top-left and top-right), M0M (bottom-left and bottom-right)
                if (grid[i - 1][j - 1] == 'S' and grid[i - 1][j + 1] == 'S' and
                    grid[i + 1][j - 1] == 'M' and grid[i + 1][j + 1] == 'M'):
                    count += 1
                    matches.append((i, j, "Orientation 3"))

                # Orientation 4: S0M (top-left and bottom-right), M0S (top-right and bottom-left)
                if (grid[i - 1][j - 1] == 'S' and grid[i + 1][j + 1] == 'M' and
                    grid[i - 1][j + 1] == 'M' and grid[i + 1][j - 1] == 'S'):
                    count += 1
                    matches.append((i, j, "Orientation 4"))

    return count

def Part2():
    return count_x_mas_all_orientations(data)
    return 0

print(f"Part 1: {Part1()}, Part 2: {Part2()}")
# submit(Part1(), session=session_id, day=4, year=2024)
submit(Part2(), session=session_id, day=4, year=2024)