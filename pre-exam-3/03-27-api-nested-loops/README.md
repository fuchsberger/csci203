## Nested For Loops

![Tic Tac Toe](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJd6tIrqyz0C3Quc9ohvlqK6DhvTXO2gJKQA&s)

Lets start by representing a game state of Tic Tac Toe in a format that the computer can read more easily. Since we always have `3` rows and `3` columns we can use a string or list, where

- `0` indicates an empty slot
- `1` indicates slot occupied by player 1 (x)
- `2` indicates slot occupied by player 2 (o)

```python
"010221100"
[0, 1, 0, 2, 2, 1, 1, 0, 0]
```

Because this game always has `3` rows and `3` columns the `index` in that list/string identifies the actual game field precicely. For example index `2` always refers to the top-right corner field.

While a string is fine we could also choose a nested list for storage:

```python
[
  [0, 1, 0],
  [2, 2, 1],
  [1, 0, 0]
]
```

A nested list is a list that contains other lists.
This is more human readable and comes with advantages and disadvantages.

We are going to write two functions now

- to convert a list in the format above into a nested list
- convert a nested list back into a singular list

```python
#  [0, 1, 0, 2, 2, 1, 1, 0, 0]

#  [
#    [0, 1, 0],
#    [2, 2, 1],
#    [1, 0, 0]
#  ]

def index_to_coordinates(index:int):
    x = index % 3
    y = index // 3

    return (x, y)

def coordinates_to_index(coords:tuple):
    x, y = coords
    # x = 2, y = 0 --> 2 (top right)
    # x = 0, y = 2 --> 6 (bottom left)
    return x + 3 * y

def tests():

    assert index_to_coordinates(2) == (2, 0)
    assert coordinates_to_index((2, 0)) == 2

if __name__ == "__main__":
    tests()
```

## Nested List indexing

```python
game =   [
    [0, 1, 0],
    [2, 2, 1],
    [1, 0, 0]
  ]

# get value at x, y: game[y][x]
print(game)
print(game[0])
print(game[0][2])
```

## Nested Loops

```python
game =   [
    [0, 1, 0],
    [2, 2, 1],
    [1, 0, 0]
  ]

# sum up all numbers in the nested list
result = 0

for row in game:
    for value in row:
        result += value

print(result)
```

### Sampe Exam Question

What will be printed?

```python
for i in range(3, 0, -1)    # 3, 2, 1
    for j in range(3):      # 0, 1, 2
        print(i + j)

# i = 3, j = 0 -> 3
# i = 3, j = 1 -> 4
# i = 3, j = 2 -> 5 done with first inner loop
# i = 2, j = 0 -> 2
# i = 2, j = 1 -> 3
# i = 2, j = 2 -> 4 done with the second inner loop
# i = 1, j = 0 -> 1
# i = 1, j = 1 -> 2
# i = 1, j = 2 -> 3 done with the second inner loop
```

## API data

In order to make the starting code work on your computer we will need to install a python module that doesn't come preinstalled:

**Windows:** Search for `cmd` or `PowerShell`. Open the program and type:

```bash
py -3.14 -m pip install requests
```

**Mac OS:** Search for `Terminal`. Open the program and type:

```bash
python3.14 -m pip install requests
```

This should install a module that allows us to send API requests to other servers!

You can then run `starting_code.py` in IDLE. You should see an output like this:

```
[38.8316650390625, -122.817169189453, 0.77]
[57.379, -156.282, 2.2]
[51.853, -172.407, 3.4]
```

_This is a very long list containing all the earthquakes measured since yesterday including their magnitude on the richter scale!_

## Scatter Plot

_We didn't get to this part in class, will do (maybe) on Wednesday_

Lets see if we can plot them in a scatter plot:

```python
import matplotlib.pyplot as pyplot

def plot(quakes: list) -> None:
    """Display a scatterplot of earthquakes.
    Parameters:
        quakes - a list of lists: [latitude, longitude, magnitude]

    Return value: None
    """
    x = []
    y = []
    for index in range(len(quakes)):
        # TODO
        pass
    pyplot.scatter(x, y) # scatter plot
    pyplot.xlabel("Latitude")
    pyplot.ylabel("Longitude")
    pyplot.show()
```
