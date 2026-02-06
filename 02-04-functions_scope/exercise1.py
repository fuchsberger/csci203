import turtle

george = turtle.Turtle()

def draw_circle(t, x, y, radius, color = "green"):
   t.up()
   t.setpos(x, y)
   t.down()
   t.fillcolor(color)
   t.begin_fill()
   t.circle(radius)
   t.end_fill()

draw_circle(george, 20, 20, 30)
draw_circle(george, 30, 40, 45, "blue")
