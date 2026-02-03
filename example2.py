import turtle

radius = int(input("Radius: "))

x = int(input("x coordinate: "))
y = int(input("y coordinate: "))

# draw a circle with the given radius at the given coordinate
# draw more circle getting smaller and smaller on top of that circle

turtle.setpos(x, y)
turtle.circle(radius)
