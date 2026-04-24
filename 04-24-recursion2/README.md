# Recursion Practice Examples:

Complete the following functions to practice recursion.
All these examples (in this length and complexity) could be featured in the final exam.

## isPalindrome(string)

A palindrome is a string that can be read from left to right and right to left without it being read differently. See tests below to see valid Palindromes.

```python
def isPalindrome(string):
  # TODO
  pass

# tests
assert isPalindrome("")
assert isPalindrome("A")
assert isPalindrome("Aa") == False
assert isPalindrome("AB") == False
assert isPalindrome("ABA")
assert isPalindrome("ABBA")
```

## buildPalindrome(string)

We can also recursively build a palindrome:

```python
def buildPalindrome(string):
  # TODO
  pass

# tests
assert buildPalindrome("") == ""
assert buildPalindrome("A") == "AA"
assert buildPalindrome("AB") == "ABBA"
```

## count(string, character)

Recursively count the number of occurences of `character` in `string`.
Note that this function has a recursive helper function to minimize the number of parameters in the main function.

```python
def count(string, character):
  return countHelper(0, string, substring)

def countHelper(count, string, character)
  # TODO
  pass

# tests
assert count("ABBA", "A") == 2
assert count("ABBA", "AB") == 1
assert count("ABBA", "BB") == 0
```

## Recursive Spiral

Recursively draw a spiral in Turtle that gets bigger (until the length of the side reaches `max_length` pixel). You may assume the increment each recursion is `5`.

```python
import turtle

g = turtle.Turtle()

def spiral(t, current_length, max_length):
  # TODO

# tests
spiral(g, 0, 120)
```

After coding this example reflect:

- What is the base case in your function?
- What is the recursive case in your function?
