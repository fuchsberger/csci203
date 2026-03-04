## Exam 2 Checklist

Note this is not a guarantee that only things from this list will come to exam 2.

Generally mostly exam 2 will feature materials we covered since exam 1 but some fundamentals (variables, functions, etc.) remain imporant throughout the semester.

- random.random, random.randint, random.choice
- monte-carlo simulations for approximation / probability prediction
- binary: converting form int/float to binary and back
- binary: demonstrating how a binary adder works
- binary: multiplying / dividing through powers of 2
- binary: AND, OR, NOT with binarys of more than a single bit

- boolean logic
    - evaluation of primitive values such as:
    - "" -> false, "test" -> true
    - 4 -> false, 0
- high level overview of how a computer works
    - flow of data between SSD, memory, CPU cache and registers
    - what is a register / ALU?
    - what is machine code, what is assembly?
    - what is a compiler?
    - python is an interpreted language. what does that mean?
    - what is a memory address. how can we find out with python?

- id() to find out memory addresses of variables
    - understand the difference between mutable and immutable datatypes and recognize them on given variables
    - understand the effects of creating a copy vs creating an alias of a variable and what that means to the memory address of the value

- accumulators and graphics
    - write the for loop and accumulating part of a given growth function
    - understand accumulating in multiple steps (e.g. 4 times per month)
    - draw a graphic based on the results of an accumulated function and given plt code

- conditional statements (if/elif/else)

### binary: AND, OR, NOT with binarys of more than a single bit

```python
a = True
b = ""
c = 0.0
d = 0.01

e = [1, 2, 3]
f = ["a"]



# all non-empty strings --> true
# empty strings --> false

## numbers not 0 --> true
## 0 --> false

## non-empty lists --> true
## empty lists --> false

##if e and f:
##    print("true")
##else:
##    print("false")

if c:
    print("DO THIS")

if c != 0:
    print("DO THAT")
```

## PI


```python
import random, math

success = 0
attempts = 1000000

for i in range(attempts):
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1

    # check if dart is in circle
    if math.sqrt(x**2 + y**2) <= 1:
        success += 1

square_area = 2 * 2
circle_area = success/attempts * square_area

print(success, attempts, round(success/attempts, 2))

## determine area of circle using monte carlo results
print(circle_area)


## result: Pi is the Area of a circle with radius 1
# validation: A = Pi * r**2

# circle_area <> pi
circumfence = r * circle_area
```
