import random
# Maze dimensions (odd values are best)
WIDTH = 15
HEIGHT = 15
# Maze symbols
WALL = 1
PATH = 0
SOLUTION = '.'
# Create a grid filled with walls
maze = [[WALL for _ in range(WIDTH)] for _ in range(HEIGHT)]
# Direction vectors (up, down, left, right)
DIRS = [(-2, 0), (2, 0), (0, -2), (0, 2)]
def is_valid(y, x):
    return 0 < y < HEIGHT-1 and 0 < x < WIDTH-1
# Recursive DFS Maze Generator
def generate_maze(y, x):
    maze[y][x] = PATH
    directions = DIRS[:]
    random.shuffle(directions)
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if is_valid(ny, nx) and maze[ny][nx] == WALL:
            maze[y + dy // 2][x + dx // 2] = PATH  # Knock down wall
            generate_maze(ny, nx)
# Recursive DFS Maze Solver
def solve_maze(y, x, end_y, end_x):
    if not is_valid(y, x) or maze[y][x] != PATH:
        return False
    if (y, x) == (end_y, end_x):
        return True
    maze[y][x] = SOLUTION  # Mark as part of solution path
    for dy, dx in DIRS:
        if solve_maze(y + dy // 2, x + dx // 2, end_y, end_x):
            return True
    maze[y][x] = PATH  # Backtrack
    return False
# Set start and end points
start_y, start_x = 1, 1
end_y, end_x = HEIGHT - 2, WIDTH - 2
# Generate and solve the maze
generate_maze(start_y, start_x)
solve_maze(start_y, start_x, end_y, end_x)
# Mark start and end
maze[start_y][start_x] = 'S'
maze[end_y][end_x] = 'E'
# Print the maze
for row in maze:
    print(' '.join(str(cell) for cell in row))
