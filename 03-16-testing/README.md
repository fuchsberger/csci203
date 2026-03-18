# Testing

Testing is super important and your testing strategy is very often probed in technical job/coding interviews.

Testing enables code quality assurance at the cost of extra development time.

Lets say we have the following function:

```python
def concatenate(a, b):
    return a + b
```

## Messy Approach

You have actually used this approach since day one:

```python
print("Expected:", "abcdef")
print("Actual:", concatenate("abc", "def"))
```

Advantages:

- fast

Disadvantages:

- mixes test code with application code
- needs to be manual removed
- always polutes console log, even when tests pass
- doesn't stop the program if test fails

## Shell Testing

Run your program normally then test things via the shell:

```shell
>>> concatenate("abc", "def")
```

Advantages:

- doesn't polute the program

Disadvantages:

- Tests have to be rewritten every time you run the program
- Only feasible for very selective, few functions
- tests only after the program already finished

Mostly used when after the program finishes you would like to inspect the values of a variable (this is also called debugging).

## Test Function

To separate tests from application code its a good idea to create separate test functions:

```python
def test():
    # test your concatenate function here with
    # either assert, print, or try/except
    pass
```

## Raising Exceptions

Its a good practice to validate inputs for correct type and correct range:

```python
def highest(numbers):
  """
  Returns the highest number in numbers.
  Numbers must be a list of non-negative integers.
  Numbers must contain at least one number.
  """
  highest = -1

  if type(numbers) != list:
    raise TypeError("Numbers must be a list")

  if len(numbers) == 0:
      raise ValueError("Numbers must contain at least one number.")

  for number in numbers:
      if not isinstance(number, int):
        raise TypeError("All numbers must be integers")

      if number < 0:
        raise ValueError("All numbers must be positive.")

      if number > highest:
        highest = number

  return highest
```

We have overdone testing here but this example shows you several things:

- how to raise Execptions
- when to use `TypeErrors` and `ValueErrors`
- checking type of a variable via `isinstance` and/or `type()` function

Raising Execptions is typically done with generic input parameters. Often manually raising exeptions is not needed as Python does it automatically:

```python
x = 5
y = 0

# not needed
if y == 0:
  raise ZeroDivisionError("division/0 is not allowed")

z = x / y

# ZeroDivision will be automatically raised when called:
z = x / y
```

## Unittests

Python provides the `assert` statement for testing:

```
assert <condition>, <message>
```

If the condition is true, nothing happens.
If the condition is false it will raise an `AssertionError` with your message.

```python
def test():
    assert concatenate("abc", "def") == "abcde", "Does not match"
```

Advantages:

- doesn't polute the program with successful tests
- stops the program if a test fails
- can be cleanly left in the application code without harm
- shows line numbers, traceback and the condition that was used

Disadvantages:

- Can only see one failed test at a time (as the program stops on fail)

## Docstring Testing

We haven't covered that but its a method for writing function call examples in the docstrings and making python run these. Makes docstrings more verbose but also shows examples which is nice.

## Unittest Framework

The most sophisticated approach that usually separates test code in separate files. For example:

```bash
myMath.py
myMath_test.py # <-- test code goes here
```

A test module could look like this:

```python
import unittest
from myMath import concatenate

class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)

    def test_concatenate(self):
        self.assertEqual(concatenate("abc", "def"), "abcde")


suite = unittest.TestLoader().loadTestsFromTestCase(TestMath)
runner = unittest.TextTestRunner(verbosity=0)
result = runner.run(suite)
print(f'Tests run: {result.testsRun}')
```

Advantages:

- Test code is completely separate from applicaiton code
- Tests can be written before application (test-driven development)
- Unlike basic `assert` statements, all tests are executed, even if they fail
- Provides a list and summary of how many tests were run and how many were successful
- can autodetect test files and run all of them with a single command
- has a couple of helper functions such as `assertRaises`, `assertIsInstance`

Disadvantages:

- most extra work to implement
