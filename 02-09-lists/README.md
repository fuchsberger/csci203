# For Loop Exercise

Handout in class (exam practice)
[https://docs.google.com/document/d/1Y6Lc9J_wWnD6tyrBAyRK7kp6QljdxjADiGzSr03XjKk](https://docs.google.com/document/d/1Y6Lc9J_wWnD6tyrBAyRK7kp6QljdxjADiGzSr03XjKk)

# Lists

A (python) list is a datatype that allows for storing multiple values in a speecific order:

```python
numbers = [1, 2, 3]
```

We can identify a list by square brackets `[`, `]` and comma separated values.

We can also create empty lists or use variables as elements of a list:

```python
items = [] # empty list
x = 3
numbers = [1, x, 5]
```

# Iterating over lists

We can loop over lists and so something with each item:

```python
def print_sum(numbers):
  """Given a list of numbers, prints the total sum.

  Parameters:
    - `numbers`, a list of float and/or integer numbers

  Return Value:
    - None
  """
  total = 0
  # we loop n times where n is the number of items in the list
  # every time we loop, number will take the value of the current item in the list
  for number in numbers:
    total = total + number
  print(total)
```

### Example 1

Complete the list assignment such that

- it contains at least 3 items
- `x` is used as a value inside the list
- the function call prints `8`

```python
x = 3
numbers = [                     ] # <-- TODO
print_sum(numbers)
```
