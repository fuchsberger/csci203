def zero_count_sorted(sorted_numbers):
  total = 0

  for number in sorted_numbers:

    if number > 0:
      return total

    if number == 0:
      total = total + 1

  return total
