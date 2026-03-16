# Testing


# concatenate("abc", "def") -> "abcdef"
def concatenate(a, b):
    return a + b


# messy approach for testing
#print(concatenate("abc", "def"))

# shell testing
# >>> concatenate("abc", "def")

# separate testing function, better!
#def test():
#   print(concatenate("abc", "def"))


# testing via assert <condition> message
#assert concatenate("abc", "def") == "abcde", \
#      "Does not match"

# testing with a test function and assert
def test():
    """

    # Examples

    >>> concatenate("a", "b")
    "ab"
    """
    assert concatenate("abc", "def") == "abcde", \
       "Does not match"

# test()

## assert:
# - only shows error if test fails
# - stops program if test fails
# - shows line number and conditon that was checked

# unittesting


import unittest

class TestMath(unittest.TestCase):
  def test_addition(self):
    self.assertEqual(2 + 2, 4)
    print('Addition test passed')

  def test_concatenate(self):
      self.assertEqual(concatenate("abc", "def"), "abcde")
      print('Concatenation test passed')


suite = unittest.TestLoader().loadTestsFromTestCase(TestMath)
runner = unittest.TextTestRunner(verbosity=0)
result = runner.run(suite)
print(f'Tests run: {result.testsRun}')
