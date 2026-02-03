# 1. Import


## 1.1 Import everything
```python
from turtle import *

forward(100) # <-- you can now directly call functions from Turtle
```
This approach is useful if you are sure working with a single library.

## 1.2 Selective Import
```python
from turtle import forward, left

forward(100) # <-- you can now directly call functions from Turtle
```
This approach is useful if you only need to import a few specific functions.

## 1.3 Alias

```python
import turtle

turtle.forward(100) # <-- you can now directly call functions from Turtle
```
This is the cleanest, but must verbose way to import.You must prepend each function call with the name of the library.

# 2. Input

You can pause the program and ask for user input:

```python
name = input("What is your name? ")
age = int(input("How old are you? "))
```
Notice that all input data comes in as a string. We need to manually convert numbers via `float()` or `int()`.

```python
age = int(input("How old are you? "))
print("You have", 81 - age, "more years to live.")
```

## 2.1 Exercise: Multiple inputs via loop

**Objective:** Write a program that asks for 5 numbers and prints out the sum.

THe solution can be found under `inputs_with_loops.py`

# 3. Turtle - More Commands

## Challenging Objective:

```python
import turtle

radius = int(input("Radius: "))

x = int(input("x coordinate: "))
y = int(input("y coordinate: "))

# draw a circle with the given radius at the given coordinate
# draw more circle getting smaller and smaller on top of that circle.
```
