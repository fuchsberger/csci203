# Exam 1 Topics

- creating a pseudoalgorithm for a given problem
- translating a pseudoalgorithm to python code
- creating a trace table from a pseudo algorithm
- creating a trace table from a python algorithm
- 4 key goals when designing an algorithm
- primitive datatypes (int, float, string, boolean)
- variable assignment and reassigment
- simply aritmethic with int, float and variables
- string concatenation
- print (comma separated and/or concatenated strings/variables)
- str(), int(), and float()
- 3 different ways to import
- for loops with range(stop)
- for loops with range(start, stop)
- for loops with range(start, stop, increment)
- for loops over a list
- What is an ADT?
- turtle graphics - understanding commands we have used in lab and exercises
- drawing a picture given a python turtle code algorithm
- writing a python turtle code algrithm given a picture
- local/global scope of variables and functions
- function definitions
- function parameters/inputs
- function return values/outputs
- function calls
- function parameters vs arguments
- main() and its purpose
- accumulators
- finding errors/problems with a given program

# Function Return statemens

A return statement has two purposes:

- immediatly exit the function (including loops if we are in one)
- (optionally) _return_ data back to the calling function.

A function can have multiple return statements.
If a function doesn't have a return statement it returns `None` by default:

```python
def contains_zero(numbers):
  for n in numbers:
    if n == 0: # we will learn more about if statements next week
      # if we encounter a 0 we can immediatly answer with True,
      # and don't need to finish checking all remaining numbers.
      # This makes the algorithm more efficient!
      return True

  # if i missed the following line, the function would have
  # returned None if 0 is not among numbers.
  return False
```

Reflection Question: What would have happend if we accidentally had `return False` nested under the for loop (below the if block)?

## Exercise 1

Write a function that returns the number of occurences of `0` in a list of numbers.

# Returning multiple things at a time:

```python
def swap(item1, item2):
  return item2, item1

a = True
b = False

a, b  = swap(a, b)

# will print: False, True
print(a, b)
```
