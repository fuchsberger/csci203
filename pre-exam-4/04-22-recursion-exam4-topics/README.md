# Exam 4 - Topics

- Exam will be 4 pages long instead of 5 and graded out of 40 points. (shorter due to less lectures since exam 3)
- Exam will count as much as the previous exams
- Exam questions might be a bit easier (subjective to say at this point)
- You should still prepare to the best of your abilities.

### Page 1 - Dictionaries and Nested Structures

- Dictionaries VS Lists
  - Know when which is appropriate
  - be able to create them (empty and prefilled)
  - be able to update key/value pairs
  - be able to index them
  - loop through them via `.keys()`, `.values()`, and `.items()`
  - understand mutability/immutability in dictionaries (keys are immutable but values are mutable)

- nested structures
  - lists of dictionaries
  - lists of lists
  - lists of tuples

  - You should be familiar with:
    - looping through 2-dimensional nested structures
    - indexing and modifying cells in a 2d structure (double indexing)
    - use them in the contexts seen in the examples (e.g)
    - time complexity for such and and similar operations

- <s>Game of Life</s>
  - <s>given (potentially modified) game of life rules, a game state (white/black cells), and a 5x5 grid be able to draw the next game state</s>

### Page 2 - Image Processing and Nested Structures

- be able to modify a function to apply a filter that is describe (like in the workshop)
- given a complete filter function (featured in the workshop or similar) be able to determine what the filter does
- be able to draw an image using a nested loop and instructions on how it should look like

### Page 3 - Recursion

- create (simple) recursive functions given a description of how it should work
- create (simple) recursive functions given the iterative equivalent
- create (simple) recursive functions given an example output sequence
- be able to determine the output of a recursive function given the function definition and a function call.
- analyze the time complexity of recursive functions

### Page 4 - Fractals

- given a (simple) Lindenmayer system, be able to draw the resulting graphic on level 1, 2, and 3
- given a (simple) graphic (level 0, 1, and 2), understand the recursive pattern ands derive the recursive function in either Lindenmayer Notation or Python code (student's choice)

# Project - Changes

Please consult the updated [Project Rubric](https://docs.google.com/spreadsheets/d/1e6pTpGP58kv9knUV6GHU1ibA9mT7kVpu-F3mV9KHpco/edit?gid=1238942540#gid=1238942540)

- I reduced the required number of choices from `5` to `3` and slighlty modified the rubric to accomodate for that change.
- This should allow you more flexibility to focus on what you want to do with less pressure on what you have to do.
- **Reminder:** Keep your project simple, I am looking primarily for your ability to apply what you have learned in your own context, not something grand and impressive!
- Progress Report 2 has been published. This will be the last progress report before project is due.

### End of Semester Easing

- I will scratch homework exercises (not readings) after exam 4 to give you more time to focus on your projects instead. They will still be published as _optional_ in case you like to attempt them for exam preparation.
- During classes following exam 4 we will spend aproximately 20-30 minutes introducing the designated topic and then switch over to worktime for your final projects. Be encouraged to ask questions during this period.
- Recursive Binary Search and Tower of Hanoi will still be viable final exam topics but only to the extend we covered them in class and in the readings.

# Recursion

A recursive function is a function that has at least one base case and one recursive case:
```python
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * (n-1)!
    else:
        return n * factorial(n - 1)

# Example usage
print(factorial(5))  # Output: 120
```
A recursive function must eventually always reach a base case, otherwise its becomes an infinte loop. Unlike iteration this causes a `RecursionError` exception after a certain depth (usually 5000).

## Activity
Convert the iterative `multiply()` function to a recursive version:

```python
def multiply(x, y):
  total = 0

  for i in range(y):
    total += x

  return total
```

```python
def multiply_rec(x, y):
  # TODO
  pass
```

## Recursive Helper functions
Sometimes when designing functions we end up with "trigger" function and a recursive helper function:

```python
def sum_list(numbers):
    # trigger function
    return sum_helper(numbers, 0)

def sum_helper(numbers, index):
    # recursive helper function
    if index == len(numbers):
        return 0
    return numbers[index] + sum_helper(numbers, index + 1)

print(sum_list([4, 7, 2, 5]))   # 18
```

The purpose of this "split" is mainly to simplify (reduce) the required parameters when callin the recursive function.


