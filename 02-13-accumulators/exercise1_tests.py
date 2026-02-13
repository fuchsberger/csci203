from exercise1 import training_cost

def main():
  expected = 11850
  actual = training_cost(20, 50)

  print("Testing training_cost(20, 50)")
  print("Expected: ", expected)
  print("Actual: ", actual)

main()
