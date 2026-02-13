# Write a function that returns the number of occurences
# of 0 in a list of numbers.

def zero_count(numbers):
  total = 0
  for number in numbers:
    if number == 0:
      total = total + 1

  return total
