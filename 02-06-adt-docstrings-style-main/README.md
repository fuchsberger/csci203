## ADT

```text
TODO in class
```

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

## Functions: Docstrings

```python
# TODO
```

## Functions: Return Value

Functions may give information back to the main program:

```python
# TODO
```

### Exercise 2

Try out the following program:

```python
def ceasar(message):
    """
    TODO by students...
    """
    result = ""
    for letter in message:
        code = ord(letter)
        new_code = code + 1
        new_letter = chr(new_code)
        result = result + new_letter
    return result

def main():
  greeting = "Hello"

  print(greeting)
  print(ceasar(greeting))

main()
```

Observe the shell output.
Your objective is to deduce what this function does and provide an appropriate docstring, including a description of the parameters and what it returns.

#### Tips

- Do not ask AI or search for what `ord()` and `char()` do.
- Instead be curious and try the following out in your program deduce from there:

```python
print(ord("A"))
print(ord("B"))
print(ord("C"))
print(chr(65))
print(chr(66))
print(chr(67))
```

What seems to be the purpose of the ord() function?
What seems to be the purpose of the chr() function?

### Exercise 3:

Based on the `encyrpt()` function you have seen. Write a function `decrypt()` that will reverse what the function encrypt() does:
```python
def decrypt(message):
  pass
```
