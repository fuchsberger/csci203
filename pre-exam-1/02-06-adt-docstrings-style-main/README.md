## ADT

An ADT is a detailed descripton of a data structure and how it behaves.
It should contain information of the functions it has and how data is stored.

**Example 1:** Custom ADT

A shopping Bag (also called a stack)

- can store multiple items up until it is full.
- function: add something to the bag
- function: remove the most recently added item

**Example 2** Python Native ADT: an Integer

- Stores a Full Number, size only limited by available Memory
- provides functions for aritmethic operations

## main function

Lets take a look back at how we ended up organizing our program from last lecture:

```python
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
```

This program is now perfectly fine but it is very common (and good practice) to have an **Entry Point** to our program so every developer can see where actual code execution starts. This is done via a `main()` function. An added benefit is that we can avoid global variables this way.

The purpose of a main function is to set up our program (if it needs configuration) and then wrap all function calls that are on global scope.

We end our program in the very last line with a call to `main()` itself.

### Exercise 1

Modify the program above to use a main function, while still displaying both circles.

The solution can be found under `exercise1.py`.

## Functions: Docstrings, iterating over lists

```python
def print_sum(numbers):
  """Given a list of numbers, prints the total sum.

  Parameters:
    - `numbers`, a list of float and/or integer numbers

  Return Value:
    - None
  """
  total = 0
  for number in numbers:
    total = total + number
  print(total)
```

A proper docstring should have the following three components:

- A 1/2 liner describing the **purpose** of the function
- A list of _parameters_ and a short description of them
- The _return_ value of the function

There are no exact rules on how to format your docstring but you will want to

- keep those three in this order
- be consistent accross your program and always use the same format. For example: Don't use `'''` sometimes and othertimes `"""`

## Comments

Idealy functions are short and do exactly what the function name implies they do (and nothing else).
Thus providing a docstring is usually enough documentation for a function.

However sometimes we have more complex sections within our code or need to clarify a line that follows. In such cases a comment comes in handy:

```python
def print_sum(numbers):
  """Given a list of numbers, prints the total sum.

  Parameters:
    - `numbers`, a list of float and/or integer numbers

  Return Value:
    - None
  """
  total = 0
  for number in numbers:
    # x += 1 is a shorthand for x = x + 1
    total += number
  print(total)
```

A comment usually refers to the line that immeadiatly follows but can be on the same line:

```python
# horizontal coordinate (better)
x = 10

x = 10  # horizontal coordinate (ok)
```
