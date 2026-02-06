## Functions

Functions need to be defined before they can be used:

```python
def print_sum(number1, number2):
  print(number1 + number2)
```

Then they can be **called**:

```python
x = 2
name_of_function(11, x)
# 13
```

### Parameters vs Arguments

#### Parameters

`number1` and `number2` are called **parameters**.
Parameters are variables that

- are created the moment a function is called
- only exist in the _scope_ of the function while it is being executed
- are destroyed (removed) the moment the function finishes/returns

#### Arguments

`11` and `2` are the **arguments** and the actual `values` or `inputs` that get passed into the function.

- `number1` will now have the value `11`
- `number2` will now have the value `2`, which comes from the variable `x`

#### Careful! Avoid the following:

```python
x = True
def do_that(x):
  print(x)
```

Its easy to think here that `x` in the first line and the parameter `x` from the function are one and the same. This could not be more wrong, they are completely independent based on the concepts outlined above.

Its probably best to avoid naming variables in your program the same as parameters in functions.

### Default Arguments

Functions may have default arguments:

```python
def name(first_name = "John", last_name = "Shepard"):
  print(first_name, last_name)
```

We can call the function above in the following ways:

```python
name("Sam", "Adams")  # will print "Sam Adams"
name("Sam")           # will print "Sam Shepard"
name()                # will print "John Shepard"
```

Optional parameters should be ordered on the right side of the inputs, with the least important one to the right most.

This is because when we have multiple optional parameters missing, Python will start filling in default arguments from the right.

We can also mix required and optional parameters:

```python
def name(first_name, last_name = ""):
  print(first_name, last_name)
```

We can call this the following way:

```python
name("Sam", "Adams")  # -> Sam Adams
name("Sam")           # -> Sam

# We can't do this now:
name()                # ERROR! Argument missing!
```

## Scope

We separate two `scopes` in python:

- `global scope`
- `function scope` (local)

```python
# the following variable is not inside a function, thus on global scope:
x = "Hello"

# that applies to functions as well, they should always be on global scope:
def do_this():
  pass

def name(first_name):
  # both first_name and last_name are local to the name function and thus
  # only exist during a function call within the name function.
  last_name = "Shepard"
  print(first_name, last_name)
```

An easy way to identify if you are on global scope is to see if the current line has any intendation or not.

Example from the Reading:

```python
def bloom(tortoise, fill_color, length):
  def stem(tortoise, length):
    pass

  stem(tortoise, length)
```

**Never nest functions inside each other!** The inner function would only be accessible from within bloom. Functions should always be on _global_ scope.

### Exercise 1: Organizing Code into functions

**Objective:** organize the following algorithm by using a function to avoid repetition and code clarity:

```python
import turtle

george = turtle.Turtle()

george.up()
george.set_pos(20, 20)
george.down()
george.fillcolor("green")
george.begin_fill()
george.circle(30)
george.end_fill()
george.up()
george.set_pos(30, 40)
george.down()
george.fillcolor("blue")
george.begin_fill()
george.circle(45)
george.end_fill()
```

#### General Procedure

- identify repeating blocks of code (may have some variety in variable values such as `radius`, `x`, or `y`).
- create a function with an appropriate name and copy over the repeating lines.
- provide variable parts as input variables (parameters) and replace the hard-coded values in the text with them.
- add a function call(s) with the actual values after your function definition
- get rid of the original relevant code that is not in a function

A solution is provide under `exercise1.py`.
