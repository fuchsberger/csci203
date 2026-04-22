def multiply_rec(x, y):
  # base case 1
  if y == 0:
      return 0
  # base case 2
  elif y == 1:
      return x
  else:
      return x + multiply_rec(x, y-1)


print(multiply_rec(4,8))
