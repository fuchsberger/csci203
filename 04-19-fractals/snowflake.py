import turtle

screen = turtle.Screen()
screen.tracer(0)   # turn off animation

def Koch(n, length):
  t = turtle.Turtle()

  # K' ++ K' ++ K'
  KochHelper(t, n, length)
  t.right(120)
  KochHelper(t, n, length)
  t.right(120)
  KochHelper(t, n, length)

def KochHelper(t, n, length):
  if n == 0:
    # F
    t.forward(length)
  else:
    # K' - K' ++ K' - K'
    KochHelper(t, n-1, length/3)
    t.left(60)
    KochHelper(t, n-1, length/3)
    t.right(120)
    KochHelper(t, n-1, length/3)
    t.left(60)
    KochHelper(t, n-1, length/3)

Koch(4, 200)

screen.update()
turtle.exitonclick()
