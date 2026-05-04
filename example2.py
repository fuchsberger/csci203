import turtle

t = turtle.Turtle()

def fu(t, depth, length):
  if depth == 0:
    t.forward(length)
  else:
    t.forward(length)
    t.left(120)
    fu(t, depth - 1, length / 2)


fu(t, 4, 100)

input()
