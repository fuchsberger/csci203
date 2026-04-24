import turtle

# 1 = open path, 0 = wall
grid = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],   # wall in the middle
    [1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1]
]

CELL_SIZE = 40
ROWS = len(grid)
COLS = len(grid[0])

screen = turtle.Screen()
screen.setup(600, 600)
screen.tracer(0)

# Turtle for drawing the grid
drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(0)
drawer.penup()

# Turtle for drawing the DFS path
walker = turtle.Turtle()
walker.shape("turtle")
walker.color("red")
walker.speed(1)
walker.pensize(2)

def cell_top_left(row, col):
    x = -COLS * CELL_SIZE / 2 + col * CELL_SIZE
    y = ROWS * CELL_SIZE / 2 - row * CELL_SIZE
    return x, y

def cell_center(row, col):
    x = -COLS * CELL_SIZE / 2 + col * CELL_SIZE + CELL_SIZE / 2
    y = ROWS * CELL_SIZE / 2 - row * CELL_SIZE - CELL_SIZE / 2
    return x, y

def draw_square(row, col, color):
    x, y = cell_top_left(row, col)
    drawer.goto(x, y)
    drawer.setheading(0)
    drawer.pendown()
    drawer.fillcolor(color)
    drawer.begin_fill()
    for _ in range(4):
        drawer.forward(CELL_SIZE)
        drawer.right(90)
    drawer.end_fill()
    drawer.penup()

def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 0:
                draw_square(row, col, "black")   # wall
            else:
                draw_square(row, col, "white")   # open space

visited = set()

def move_to_cell(row, col):
    x, y = cell_center(row, col)
    walker.goto(x, y)

def dfs(row, col):
    # stop if outside the grid
    if row < 0 or row >= ROWS or col < 0 or col >= COLS:
        return

    # stop if this is a wall
    if grid[row][col] == 0:
        return

    # stop if already visited
    if (row, col) in visited:
        return

    visited.add((row, col))

    # move turtle to this cell
    move_to_cell(row, col)

    # explore neighbors
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < ROWS and 0 <= new_col < COLS:
            if grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                dfs(new_row, new_col)

                # after recursive call, come back to current cell
                # so you can see the turtle "walk around" and backtrack
                move_to_cell(row, col)

draw_grid()

# start turtle at the first cell
walker.penup()
move_to_cell(0, 0)
walker.pendown()

dfs(0, 0)

screen.update()
turtle.done()
