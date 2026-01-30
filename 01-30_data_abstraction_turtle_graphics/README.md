# What makes a "good" algorithm?

1. Efficiency (Speed, Memory)
2. Simplicity (Maintainability, Collaboration)
3. Correctness
4. Ethical considerations

# Intro Loops

```python
for i in range(100):
   print(i)

# range() - function call
# parameters (0, 100) - the input values
for i in range(0, 100):
   print(i)

# def... - function definition
# arugments (start, end) - the input names
# start is always included, end is always excluded
# increment and start are ommited by default
def range(start = 0, end, increment = 1):
   # algorithm
   return output
```

### Exercise 1 - "Zapfen"

_Don't attempt before we get there in class._

```txt
      77
* 2   154
* 3   462
* 4   1848
* 5   9240
* 6   55440
* 7   388080
* 8   3104640
* 9   27941760
/ 2   13970880
/ 3   4656960
/ 4   1164240
/ 5   232848
/ 6   38808
/ 7   5544
/ 8   693
/ 9   77
```

You will find the solution under `zapfen.py`

# Intro Turtle Graphics

Turtle allows us to paint a line with an algorithm!

```python
# import the turtle module first
from turtle import *

forward(100)   # moves forward 100px
left(90)       # turns left 90 degrees
```

[Turtle Graphics Documentation](https://docs.python.org/3/library/turtle.html)

**Careful.** Don't name your file the same as a standard library such as `math.py` or `turtle.py`. If you do, you won't be able to import `turtle` and you get warnings/errors.

### Exercise 2

_Don't attempt before we get there in class._

Attempt to recreate the following spiral using what you have learned.
Remember to follow the best practices of a good algorithm.

![Spiral](spiral.png)

You will find the solution to this under `spiral.py`.
