number = 77

print("     ", number)
for i in range(2, 10):
  number = number * i
  print("*", i, " ", number)

for i in range(2, 10):
  number = number // i
  print("/", i, " ", number)


