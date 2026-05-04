# create a recursive function
# that places a plus on a given grid and starting coordinate




def plus(grid, x, y):
  rec_row(grid, 0, 1)
  # do the same for col

# you may need recursive helpers for that.
def rec_row(grid, x, y):
  if x == len(grid[0]) - 1:
    grid[y][x] = 1
  else:
    grid[y][x] = 1
    rec_row(grid, x + 1, y)


## TEST Function
def main():
  # set up empty grid
  grid = []
  for i in range(4):
    grid.append([0, 0, 0, 0])

  # mutate it
  plus(grid, 2, 1)

  print(grid)

main()
