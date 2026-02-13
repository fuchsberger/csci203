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

```python
def count_zero(numbers):
  # TODO: Code this
  pass
```

The solution can be found in `exercise1.py`

## Exercise 2

Assuming numbers are sorted in ascending order can we make this algorithm more efficient?

```python
def count_zero_sorted(numbers):
  # TODO: code this
  pass
```

The solution can be found in `exercise2.py`

# Properly Testing a function

A good way to test a function is to create a separate test file and then import your actual file (make sure its in the same directory):

```python
# exercise2_tests.py

from exercise2 import count_zero_sorted

def main():

  expected = 2
  actual = zero_count_sorted([-2, -1, 0, 0, 1, 2])

  print("Testing zero_count_sorted([-2, -1, 0, 0, 1, 2])")
  print("Expected: ", expected)
  print("Actual: ", actual)


main()
```

Advantages:

- Keeps your main code and tests separate.
- running your main function in `exercise1.py` doesn't also run tests.
- You don't have to clean up (comment in and out) your tests
- clear separation of responsibilities

Disadvantages:

- slightly higher overhead / complexity (need to work in a second file)

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

## Exercise 3

Modify `exercise2.py` such that it returns 2 things:

- the count of `O`s as before
- the number of loop iterations we checked

Also properly create a test file for `exercise3.py`.

Here is a test that should pass when running your function

```python
expected = 2, 5
actual = zero_count_sorted2([-2, -1, 0, 0, 1, 2])

print("Testing zero_count_sorted2([-2, -1, 0, 0, 1, 2])")
print("Expected: ", expected)
print("Actual: ", actual)
```

The solution can be found in `exercise3.py` and `exercise3_tests.py`.
