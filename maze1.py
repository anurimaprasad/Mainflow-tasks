import random

# Maze dimensions (odd numbers work best)
WIDTH = 15
HEIGHT = 15

# Symbols
WALL = '#'
PATH = ' '
START = 'S'
END = 'E'
SOLUTION = '.'

# Initialize maze full of walls
maze = [[WALL for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Direction vectors: (dy, dx)
DIRS = [(-2, 0), (2, 0), (0, -2), (0, 2)]

def is_valid(y, x):
    return 0 < x < WIDTH-1 and 0 < y < HEIGHT-1
# Recursive DFS maze generator
def generate_maze(y, x):
    maze[y][x] = PATH
    dirs = DIRS[:]
    random.shuffle(dirs)

    for dy, dx in dirs:
        ny, nx = y + dy, x + dx
        if is_valid(ny, nx) and maze[ny][nx] == WALL:
            maze[y + dy//2][x + dx//2] = PATH
            generate_maze(ny, nx)

# DFS maze solver
def solve_maze(y, x):
    if not is_valid(y, x) or maze[y][x] in (WALL, SOLUTION):
        return False
    if (y, x) == end:
        return True

    maze[y][x] = SOLUTION
    for dy, dx in DIRS:
        if solve_maze(y + dy//2, x + dx//2):
            return True

    maze[y][x] = PATH
    return False

# Generate and solve maze
start = (1, 1)
end = (HEIGHT - 2, WIDTH - 2)
generate_maze(*start)
maze[start[0]][start[1]] = START
maze[end[0]][end[1]] = END

# Solve from just outside start point
solve_maze(start[0], start[1])

# Print the maze
for row in maze:
    print(''.join(row))
