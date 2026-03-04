import turtle, random
turtle.speed(0)
turtle.tracer(0)


# IGNORE THE LINES BELOW ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
screen = turtle.Screen()
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()

# attempt to raise/focus
root.attributes("-topmost", 1)   # bring to front
root.update()
root.attributes("-topmost", 0)   # then allow normal behavior again
root.focus_force()
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


def one_step(x, y, step_length):
    r = random.random()       # randomly choose a direction
    if r < 0.25:              # if r is in [0.0, 0.25), then
        x = x + step_length   #   move east and skip ahead
    elif r < 0.5:             # otherwise, if r is in [0.25, 0.5), then
        y = y + step_length   #   move north and skip ahead
    elif r < 0.75:            # otherwise, if r is in [0.5, 0.75), then
        x = x - step_length   #   move west and skip ahead
    else:                     # otherwise,
        y = y - step_length   #   move south

    return x, y

def escape(width):
    """Compute the number of steps required for a randomly moving
       particle to escape a square room with a small open window.

    Parameter:
        width: half the width of the room

    Return value: the number of steps needed to escape
    """

    gap = width / 10           # half the width of the window

    # Draw the room using turtle graphics.
    # room = turtle.Turtle()         # draw 3 sides of the room
    # room.hideturtle()
    # room.pensize(5)
    # room.pencolor('red')
    # room.up()
    # room.goto(-width, -width)
    # room.down()
    # for side in range(3):
    #     room.forward(2 * width)
    #     room.left(90)

    # room.forward(width - gap)  # draw the wall with the door
    # room.up()
    # room.forward(2 * gap)
    # room.down()
    # room.forward(width - gap)

    # particle = turtle.Turtle()     # a Turtle representing the particle
    # particle.speed(0)
    # particle.shape('circle')       # make it half-sized circle
    # particle.shapesize(0.5)
    # particle.color('blue')

    x = 0                          # position of the particle
    y = 0
    step_length = width / 20       # length of a step
    escaped = False                # whether the particle has escaped
    num_steps = 0
    while not escaped:
        num_steps = num_steps + 1

        prev_x, prev_y = x, y
        x, y = one_step(x, y, step_length)

        # if we escape through the gap
        if x <= -width and y <= gap and y >= -gap:
            escaped = True
        # elif the particle hits a wall:
        elif x <= -width or x >= width or y <= -width or y >= width:
            #     bounce back to the previous position
            x, y = prev_x, prev_y

    #     particle.goto(x, y)

    # screen = room.getscreen()
    # screen.exitonclick()

    return num_steps

def main():
    total = 0
    for i in range(1000):
      num_steps = escape(200)
      total += num_steps

    print("Average Steps:", round(total/1000))
    turtle.done()

main()
